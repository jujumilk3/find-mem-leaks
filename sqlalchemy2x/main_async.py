import asyncio
import os
import random

import psutil
from sqlalchemy import Column, ForeignKey, Integer, String, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from tqdm import tqdm


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


def get_memory_usage():
    """현재 프로세스의 메모리 사용량을 MB 단위로 반환"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


async def perform_random_crud_operations(
    session: AsyncSession,
    num_operations: int = 10000,
    create_ratio: float = 0.25,
    read_ratio: float = 0.25,
    update_ratio: float = 0.25,
    delete_ratio: float = 0.25,
):
    """
    랜덤한 CRUD 작업을 수행하고 메모리 사용량을 측정

    Args:
        session: AsyncSession 객체
        num_operations: 총 작업 횟수
        create_ratio: 생성 작업 비율 (0-1)
        read_ratio: 읽기 작업 비율 (0-1)
        update_ratio: 수정 작업 비율 (0-1)
        delete_ratio: 삭제 작업 비율 (0-1)
    """
    total_ratio = create_ratio + read_ratio + update_ratio + delete_ratio
    if not (0.99 <= total_ratio <= 1.01):
        raise ValueError("CRUD ratios must sum to 1.0")

    operations_count = {"create": 0, "read": 0, "update": 0, "delete": 0}

    start_memory = get_memory_usage()
    print(f"Initial memory usage: {start_memory:.2f} MB")

    for i in tqdm(range(num_operations)):
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

        if operation == "create":
            post = Post(title=f"Post {i}", body=f"Body {i}")
            session.add(post)
            await session.commit()

            num_comments = random.randint(1, 3)
            for j in range(num_comments):
                comment = Comment(post_id=post.id, body=f"Comment {j} for Post {i}")
                session.add(comment)
            await session.commit()

        elif operation == "read":
            count_result = await session.scalar(select(Post.id).order_by(Post.id.desc()).limit(1))
            if count_result:
                post_id = random.randint(1, max(1, count_result))
                stmt = select(Post).where(Post.id == post_id)
                post = await session.scalar(stmt)
                if post:
                    stmt = select(Comment).where(Comment.post_id == post_id)
                    _ = (await session.scalars(stmt)).all()

        elif operation == "update":
            count_result = await session.scalar(select(Post.id).order_by(Post.id.desc()).limit(1))
            if count_result:
                post_id = random.randint(1, max(1, count_result))
                stmt = (
                    update(Post).where(Post.id == post_id).values(title=f"Updated Post {i}", body=f"Updated Body {i}")
                )
                await session.execute(stmt)
                await session.commit()

        else:  # delete
            count_result = await session.scalar(select(Post.id).order_by(Post.id.desc()).limit(1))
            if count_result:
                post_id = random.randint(1, max(1, count_result))
                stmt = delete(Post).where(Post.id == post_id)
                await session.execute(stmt)
                await session.commit()

        if (i + 1) % 1000 == 0 and DEBUG is True:
            print(f"Completed {i + 1} operations")

    end_memory = get_memory_usage()

    if DEBUG is True:
        print("\nOperation counts:")
        for operation, count in operations_count.items():
            print(f"{operation.capitalize()}: {count} ({count / num_operations * 100:.1f}%)")

        print("\nMemory usage:")
        print(f"Initial: {start_memory:.2f} MB")
        print(f"Final: {end_memory:.2f} MB")
        print(f"Difference: {end_memory - start_memory:.2f} MB")

    return {
        "initial_memory": round(start_memory, 2),
        "final_memory": round(end_memory, 2),
        "memory_diff": round(end_memory - start_memory, 2),
        "num_operations": num_operations,
        "create_ratio": create_ratio,
        "read_ratio": read_ratio,
        "update_ratio": update_ratio,
        "delete_ratio": delete_ratio,
    }


async def main(
    num_operations=10000,
    create_ratio=0.3,
    read_ratio=0.4,
    update_ratio=0.2,
    delete_ratio=0.1,
):
    engine = create_async_engine("sqlite+aiosqlite:///test.db", echo=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with async_session() as session:
        result = await perform_random_crud_operations(
            session,
            num_operations=num_operations,
            create_ratio=create_ratio,
            read_ratio=read_ratio,
            update_ratio=update_ratio,
            delete_ratio=delete_ratio,
        )
    await engine.dispose()
    return result


if __name__ == "__main__":
    DEBUG = False

    # ================= 10,000 operations =================

    for _ in range(5):
        result_10000_operations = asyncio.run(
            main(
                num_operations=10000,
                create_ratio=0.25,
                read_ratio=0.25,
                update_ratio=0.25,
                delete_ratio=0.25,
            )
        )
        print("**result_10000_operations**")
        print(result_10000_operations)

    # ================= 100,000 operations =================

    for _ in range(5):
        result_100000_operations = asyncio.run(
            main(
                num_operations=100000,
                create_ratio=0.25,
                read_ratio=0.25,
                update_ratio=0.25,
                delete_ratio=0.25,
            )
        )
        # print("result_100000_operations")
        # print(result_100000_operations)
        print(
            f"| sqlalchemy2x | result_100000_operations | {_ + 1} | {result_100000_operations['memory_diff']} | {result_100000_operations['initial_memory']} | {result_100000_operations['final_memory']} | {result_100000_operations['num_operations']} | {result_100000_operations['create_ratio']} | {result_100000_operations['read_ratio']} | {result_100000_operations['update_ratio']} | {result_100000_operations['delete_ratio']} |"
        )

    # ================= Create heavy =================

    for _ in range(5):
        result_create_heavy = asyncio.run(
            main(
                num_operations=10000,
                create_ratio=0.5,
                read_ratio=0.2,
                update_ratio=0.2,
                delete_ratio=0.1,
            )
        )
        print("result_create_heavy")
        print(result_create_heavy)
        print(
            f"| sqlalchemy2x | result_create_heavy | {_ + 1} | {result_create_heavy['memory_diff']} | {result_create_heavy['initial_memory']} | {result_create_heavy['final_memory']} | {result_create_heavy['num_operations']} | {result_create_heavy['create_ratio']} | {result_create_heavy['read_ratio']} | {result_create_heavy['update_ratio']} | {result_create_heavy['delete_ratio']} |"
        )

    # ================= Read heavy =================

    for _ in range(5):
        result_read_heavy = asyncio.run(
            main(
                num_operations=10000,
                create_ratio=0.1,
                read_ratio=0.6,
                update_ratio=0.2,
                delete_ratio=0.1,
            )
        )
        print("result_read_heavy")
        print(result_read_heavy)
        print(
            f"| sqlalchemy2x | result_read_heavy | {_ + 1} | {result_read_heavy['memory_diff']} | {result_read_heavy['initial_memory']} | {result_read_heavy['final_memory']} | {result_read_heavy['num_operations']} | {result_read_heavy['create_ratio']} | {result_read_heavy['read_ratio']} | {result_read_heavy['update_ratio']} | {result_read_heavy['delete_ratio']} |"
        )

    # ================= Update heavy =================

    for _ in range(5):
        result_update_heavy = asyncio.run(
            main(
                num_operations=10000,
                create_ratio=0.2,
                read_ratio=0.2,
                update_ratio=0.5,
                delete_ratio=0.1,
            )
        )
        print("result_update_heavy")
        print(result_update_heavy)
        print(
            f"| sqlalchemy2x | update_heavy | {_ + 1} | {result_update_heavy['memory_diff']} | {result_update_heavy['initial_memory']} | {result_update_heavy['final_memory']} | {result_update_heavy['num_operations']} | {result_update_heavy['create_ratio']} | {result_update_heavy['read_ratio']} | {result_update_heavy['update_ratio']} | {result_update_heavy['delete_ratio']} |"
        )

    # ================= Delete heavy =================

    for _ in range(5):
        result_delete_heavy = asyncio.run(
            main(
                num_operations=10000,
                create_ratio=0.1,
                read_ratio=0.2,
                update_ratio=0.2,
                delete_ratio=0.5,
            )
        )
        print("result_delete_heavy")
        print(result_delete_heavy)
        print(
            f"| sqlalchemy2x | delete_heavy | {_ + 1} | {result_delete_heavy['memory_diff']} | {result_delete_heavy['initial_memory']} | {result_delete_heavy['final_memory']} | {result_delete_heavy['num_operations']} | {result_delete_heavy['create_ratio']} | {result_delete_heavy['read_ratio']} | {result_delete_heavy['update_ratio']} | {result_delete_heavy['delete_ratio']} |"
        )
