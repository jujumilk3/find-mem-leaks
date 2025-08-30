import asyncio
import os
import random
import threading
import time

import aiohttp
import psutil
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from tqdm import tqdm
import uvicorn


Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    body = Column(String)

    post = relationship("Post", back_populates="comments")


engine = create_async_engine("sqlite+aiosqlite:///fastapi_async_scoped_1x.db", echo=False)
async_session_factory = sessionmaker(engine, class_=AsyncSession)
async_scoped_session_obj = async_scoped_session(async_session_factory, scopefunc=asyncio.current_task)

app = FastAPI()


async def get_async_scoped_db():
    async with async_scoped_session_obj() as session:
        yield session


@app.on_event("startup")
async def create_tables():
    sync_engine = create_engine("sqlite:///fastapi_async_scoped_1x.db", connect_args={"check_same_thread": False})
    Base.metadata.create_all(sync_engine)


@app.on_event("shutdown")
async def cleanup():
    """애플리케이션 종료 시 async scoped session 정리"""
    await async_scoped_session_obj.remove()
    await engine.dispose()


@app.post("/posts/")
async def create_post(title: str, body: str, db=Depends(get_async_scoped_db)):
    try:
        post = Post(title=title, body=body)
        db.add(post)
        await db.commit()
        await db.refresh(post)
        
        num_comments = random.randint(1, 3)
        for j in range(num_comments):
            comment = Comment(post_id=post.id, body=f"Comment {j} for {title}")
            db.add(comment)
        await db.commit()
        return {"post_id": post.id, "comments_created": num_comments}
    except Exception as e:
        await db.rollback()
        return {"error": "Database operation failed", "post_id": -1, "comments_created": 0}


@app.get("/posts/")
async def read_posts(db=Depends(get_async_scoped_db)):
    try:
        result = await db.execute("SELECT COUNT(*) FROM posts")
        count = result.scalar()
        if count > 0:
            post_id = random.randint(1, max(1, count))
            result = await db.execute(f"SELECT * FROM posts WHERE id = {post_id}")
            post = result.first()
            if post:
                comments_result = await db.execute(f"SELECT * FROM comments WHERE post_id = {post_id}")
                comments = comments_result.fetchall()
                return {"post_id": post.id, "title": post.title, "comments_count": len(comments)}
        return {"message": "No posts found"}
    except Exception as e:
        return {"error": "Database read failed", "message": "No posts found"}


@app.put("/posts/{post_id}")
async def update_post(post_id: int, title: str, body: str, db=Depends(get_async_scoped_db)):
    try:
        await db.execute(
            f"UPDATE posts SET title = '{title}', body = '{body}' WHERE id = {post_id}"
        )
        await db.commit()
        return {"message": "Post updated", "post_id": post_id}
    except Exception as e:
        await db.rollback()
        return {"error": "Database update failed", "post_id": post_id}


@app.delete("/posts/{post_id}")
async def delete_post(post_id: int, db=Depends(get_async_scoped_db)):
    try:
        await db.execute(f"DELETE FROM posts WHERE id = {post_id}")
        await db.commit()
        return {"message": "Post deleted", "post_id": post_id}
    except Exception as e:
        await db.rollback()
        return {"error": "Database delete failed", "post_id": post_id}


def get_memory_usage():
    """현재 프로세스의 메모리 사용량을 MB 단위로 반환"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


async def make_async_request(session, operation, base_url, operation_id):
    """단일 비동기 HTTP 요청 실행"""
    try:
        if operation == "create":
            async with session.post(
                f"{base_url}/posts/",
                params={"title": f"Post {operation_id}", "body": f"Body {operation_id}"},
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                return response.status < 500
        elif operation == "read":
            async with session.get(f"{base_url}/posts/", timeout=aiohttp.ClientTimeout(total=10)) as response:
                return response.status < 500
        elif operation == "update":
            post_id = random.randint(1, max(1, operation_id))
            async with session.put(
                f"{base_url}/posts/{post_id}",
                params={"title": f"Updated Post {operation_id}", "body": f"Updated Body {operation_id}"},
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                return response.status < 500
        else:  # delete
            post_id = random.randint(1, max(1, operation_id))
            async with session.delete(f"{base_url}/posts/{post_id}", timeout=aiohttp.ClientTimeout(total=10)) as response:
                return response.status < 500
    except Exception:
        return False


async def perform_random_crud_operations(
    base_url: str,
    num_operations: int = 10000,
    create_ratio: float = 0.25,
    read_ratio: float = 0.25,
    update_ratio: float = 0.25,
    delete_ratio: float = 0.25,
    max_concurrent: int = 50,
):
    """
    FastAPI 서버에 대해 랜덤한 CRUD 작업을 수행하고 메모리 사용량을 측정
    async_scoped_session 사용
    """
    total_ratio = create_ratio + read_ratio + update_ratio + delete_ratio
    if not (0.99 <= total_ratio <= 1.01):
        raise ValueError("CRUD ratios must sum to 1.0")

    operations_count = {"create": 0, "read": 0, "update": 0, "delete": 0}

    start_memory = get_memory_usage()
    if DEBUG:
        print(f"Initial memory usage: {start_memory:.2f} MB")

    operations = []
    for i in range(num_operations):
        remaining = num_operations - i
        current_ratios = {
            "create": (create_ratio * num_operations - operations_count["create"]) / remaining,
            "read": (read_ratio * num_operations - operations_count["read"]) / remaining,
            "update": (update_ratio * num_operations - operations_count["update"]) / remaining,
            "delete": (delete_ratio * num_operations - operations_count["delete"]) / remaining,
        }

        current_ratios = {k: max(0, v) for k, v in current_ratios.items()}
        total = sum(current_ratios.values())
        if total == 0:
            break

        current_ratios = {k: v / total for k, v in current_ratios.items()}
        operation = random.choices(list(current_ratios.keys()), weights=list(current_ratios.values()))[0]
        operations_count[operation] += 1
        operations.append((operation, i))

    successful_operations = 0
    connector = aiohttp.TCPConnector(limit=max_concurrent, limit_per_host=max_concurrent)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def bounded_request(operation, operation_id):
            async with semaphore:
                return await make_async_request(session, operation, base_url, operation_id)
        
        tasks = [
            bounded_request(operation, operation_id)
            for operation, operation_id in operations
        ]
        
        for completed_task in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            result = await completed_task
            if result:
                successful_operations += 1

    await async_scoped_session_obj.remove()

    end_memory = get_memory_usage()

    if DEBUG:
        print("\nOperation counts:")
        for operation, count in operations_count.items():
            print(f"{operation.capitalize()}: {count} ({count / num_operations * 100:.1f}%)")
        print(f"Successful operations: {successful_operations}/{num_operations}")
        print("\nMemory usage:")
        print(f"Initial: {start_memory:.2f} MB")
        print(f"Final: {end_memory:.2f} MB")
        print(f"Difference: {end_memory - start_memory:.2f} MB")

    return {
        "initial_memory": round(start_memory, 2),
        "final_memory": round(end_memory, 2),
        "memory_diff": round(end_memory - start_memory, 2),
        "num_operations": num_operations,
        "successful_operations": successful_operations,
        "create_ratio": create_ratio,
        "read_ratio": read_ratio,
        "update_ratio": update_ratio,
        "delete_ratio": delete_ratio,
    }


def run_server():
    """서버를 별도 스레드에서 실행"""
    uvicorn.run(app, host="127.0.0.1", port=8013, log_level="error")


async def wait_for_server(base_url: str, max_attempts: int = 30):
    """서버가 시작될 때까지 대기"""
    for _ in range(max_attempts):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{base_url}/docs", timeout=aiohttp.ClientTimeout(total=1)) as response:
                    if response.status == 200:
                        return True
        except Exception:
            pass
        await asyncio.sleep(1)
    return False


async def main_async(
    num_operations=10000,
    create_ratio=0.3,
    read_ratio=0.4,
    update_ratio=0.2,
    delete_ratio=0.1,
):
    base_url = "http://127.0.0.1:8013"
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    if not await wait_for_server(base_url):
        raise RuntimeError("Failed to start server")
    
    await asyncio.sleep(2)
    
    try:
        result = await perform_random_crud_operations(
            base_url,
            num_operations=num_operations,
            create_ratio=create_ratio,
            read_ratio=read_ratio,
            update_ratio=update_ratio,
            delete_ratio=delete_ratio,
        )
        return result
    except Exception as e:
        print(f"Error during operations: {e}")
        return None


def main(num_operations=10000, create_ratio=0.3, read_ratio=0.4, update_ratio=0.2, delete_ratio=0.1):
    return asyncio.run(main_async(num_operations, create_ratio, read_ratio, update_ratio, delete_ratio))


if __name__ == "__main__":
    DEBUG = False

    # ================= 10,000 operations =================

    for _ in range(5):
        result = main(
            num_operations=10000,
            create_ratio=0.25,
            read_ratio=0.25,
            update_ratio=0.25,
            delete_ratio=0.25,
        )
        if result:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | 10000_operations | ✅ | {_ + 1} | "
                f"{result['memory_diff']} | {result['initial_memory']} | "
                f"{result['final_memory']} | {result['num_operations']} | "
                f"{result['create_ratio']} | {result['read_ratio']} | "
                f"{result['update_ratio']} | {result['delete_ratio']} |"
            )

    # ================= 100,000 operations =================

    for _ in range(5):
        result = main(
            num_operations=100000,
            create_ratio=0.25,
            read_ratio=0.25,
            update_ratio=0.25,
            delete_ratio=0.25,
        )
        if result:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | 100000_operations | ✅ | {_ + 1} | "
                f"{result['memory_diff']} | {result['initial_memory']} | "
                f"{result['final_memory']} | {result['num_operations']} | "
                f"{result['create_ratio']} | {result['read_ratio']} | "
                f"{result['update_ratio']} | {result['delete_ratio']} |"
            )


    # ================= Create heavy =================
    for _ in range(5):
        result_create_heavy = main(
            num_operations=10000,
            create_ratio=0.5,
            read_ratio=0.2,
            update_ratio=0.2,
            delete_ratio=0.1,
        )
        if result_create_heavy:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | create_heavy | ✅ | {_ + 1} | "
                f"{result_create_heavy['memory_diff']} | {result_create_heavy['initial_memory']} | "
                f"{result_create_heavy['final_memory']} | {result_create_heavy['num_operations']} | "
                f"{result_create_heavy['create_ratio']} | {result_create_heavy['read_ratio']} | "
                f"{result_create_heavy['update_ratio']} | {result_create_heavy['delete_ratio']} |"
            )

    # ================= Read heavy =================
    for _ in range(5):
        result_read_heavy = main(
            num_operations=10000,
            create_ratio=0.1,
            read_ratio=0.6,
            update_ratio=0.2,
            delete_ratio=0.1,
        )
        if result_read_heavy:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | read_heavy | ✅ | {_ + 1} | "
                f"{result_read_heavy['memory_diff']} | {result_read_heavy['initial_memory']} | "
                f"{result_read_heavy['final_memory']} | {result_read_heavy['num_operations']} | "
                f"{result_read_heavy['create_ratio']} | {result_read_heavy['read_ratio']} | "
                f"{result_read_heavy['update_ratio']} | {result_read_heavy['delete_ratio']} |"
            )

    # ================= Update heavy =================
    for _ in range(5):
        result_update_heavy = main(
            num_operations=10000,
            create_ratio=0.2,
            read_ratio=0.2,
            update_ratio=0.5,
            delete_ratio=0.1,
        )
        if result_update_heavy:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | update_heavy | ✅ | {_ + 1} | "
                f"{result_update_heavy['memory_diff']} | {result_update_heavy['initial_memory']} | "
                f"{result_update_heavy['final_memory']} | {result_update_heavy['num_operations']} | "
                f"{result_update_heavy['create_ratio']} | {result_update_heavy['read_ratio']} | "
                f"{result_update_heavy['update_ratio']} | {result_update_heavy['delete_ratio']} |"
            )

    # ================= Delete heavy =================
    for _ in range(5):
        result_delete_heavy = main(
            num_operations=10000,
            create_ratio=0.1,
            read_ratio=0.2,
            update_ratio=0.2,
            delete_ratio=0.5,
        )
        if result_delete_heavy:
            print(
                f"| sqlalchemy1x_fastapi_async_scoped | delete_heavy | ✅ | {_ + 1} | "
                f"{result_delete_heavy['memory_diff']} | {result_delete_heavy['initial_memory']} | "
                f"{result_delete_heavy['final_memory']} | {result_delete_heavy['num_operations']} | "
                f"{result_delete_heavy['create_ratio']} | {result_delete_heavy['read_ratio']} | "
                f"{result_delete_heavy['update_ratio']} | {result_delete_heavy['delete_ratio']} |"
            )