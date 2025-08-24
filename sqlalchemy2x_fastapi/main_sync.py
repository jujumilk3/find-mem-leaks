import os
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import psutil
import requests
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, delete, select, update
from sqlalchemy.orm import DeclarativeBase, Session, relationship, sessionmaker
from tqdm import tqdm
import uvicorn


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    body = Column(String)

    post = relationship("Post", back_populates="comments")


engine = create_engine("sqlite:///fastapi_sync.db", echo=False, pool_pre_ping=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/")
def create_post(title: str, body: str, db: Session = Depends(get_db)):
    post = Post(title=title, body=body)
    db.add(post)
    db.commit()
    db.refresh(post)
    
    num_comments = random.randint(1, 3)
    for j in range(num_comments):
        comment = Comment(post_id=post.id, body=f"Comment {j} for {title}")
        db.add(comment)
    db.commit()
    return {"post_id": post.id, "comments_created": num_comments}


@app.get("/posts/")
def read_posts(db: Session = Depends(get_db)):
    count_result = db.scalar(select(Post.id).order_by(Post.id.desc()).limit(1))
    if count_result:
        post_id = random.randint(1, max(1, count_result))
        stmt = select(Post).where(Post.id == post_id)
        post = db.scalar(stmt)
        if post:
            stmt = select(Comment).where(Comment.post_id == post_id)
            comments = db.scalars(stmt).all()
            return {"post_id": post.id, "title": post.title, "comments_count": len(comments)}
    return {"message": "No posts found"}


@app.put("/posts/{post_id}")
def update_post(post_id: int, title: str, body: str, db: Session = Depends(get_db)):
    stmt = update(Post).where(Post.id == post_id).values(title=title, body=body)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post updated", "post_id": post_id}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    stmt = delete(Post).where(Post.id == post_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted", "post_id": post_id}


def get_memory_usage():
    """현재 프로세스의 메모리 사용량을 MB 단위로 반환"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def make_request(operation, base_url, operation_id):
    """단일 HTTP 요청 실행"""
    try:
        if operation == "create":
            response = requests.post(
                f"{base_url}/posts/",
                params={"title": f"Post {operation_id}", "body": f"Body {operation_id}"},
                timeout=10
            )
        elif operation == "read":
            response = requests.get(f"{base_url}/posts/", timeout=10)
        elif operation == "update":
            post_id = random.randint(1, max(1, operation_id))
            response = requests.put(
                f"{base_url}/posts/{post_id}",
                params={"title": f"Updated Post {operation_id}", "body": f"Updated Body {operation_id}"},
                timeout=10
            )
        else:  # delete
            post_id = random.randint(1, max(1, operation_id))
            response = requests.delete(f"{base_url}/posts/{post_id}", timeout=10)
        
        return response.status_code < 500
    except Exception:
        return False


def perform_random_crud_operations(
    base_url: str,
    num_operations: int = 10000,
    create_ratio: float = 0.25,
    read_ratio: float = 0.25,
    update_ratio: float = 0.25,
    delete_ratio: float = 0.25,
    max_workers: int = 10,
):
    """
    FastAPI 서버에 대해 랜덤한 CRUD 작업을 수행하고 메모리 사용량을 측정
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
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(make_request, operation, base_url, operation_id)
            for operation, operation_id in operations
        ]
        
        for future in tqdm(as_completed(futures), total=len(futures)):
            if future.result():
                successful_operations += 1

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
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")


def wait_for_server(base_url: str, max_attempts: int = 30):
    """서버가 시작될 때까지 대기"""
    for _ in range(max_attempts):
        try:
            response = requests.get(f"{base_url}/docs", timeout=1)
            if response.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False


def main(
    num_operations=10000,
    create_ratio=0.3,
    read_ratio=0.4,
    update_ratio=0.2,
    delete_ratio=0.1,
):
    base_url = "http://127.0.0.1:8000"
    
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    if not wait_for_server(base_url):
        raise RuntimeError("Failed to start server")
    
    time.sleep(2)
    
    try:
        result = perform_random_crud_operations(
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
                f"| sqlalchemy2x_fastapi_sync | 10000_operations | ✅ | {_ + 1} | "
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
                f"| sqlalchemy2x_fastapi_sync | 100000_operations | ✅ | {_ + 1} | "
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
                f"| sqlalchemy2x_fastapi_sync | create_heavy | ✅ | {_ + 1} | "
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
                f"| sqlalchemy2x_fastapi_sync | read_heavy | ✅ | {_ + 1} | "
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
                f"| sqlalchemy2x_fastapi_sync | update_heavy | ✅ | {_ + 1} | "
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
                f"| sqlalchemy2x_fastapi_sync | delete_heavy | ✅ | {_ + 1} | "
                f"{result_delete_heavy['memory_diff']} | {result_delete_heavy['initial_memory']} | "
                f"{result_delete_heavy['final_memory']} | {result_delete_heavy['num_operations']} | "
                f"{result_delete_heavy['create_ratio']} | {result_delete_heavy['read_ratio']} | "
                f"{result_delete_heavy['update_ratio']} | {result_delete_heavy['delete_ratio']} |"
            )