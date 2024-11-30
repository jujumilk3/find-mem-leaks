from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import asyncio
import random
import psutil
import os
from typing import List


# define models
Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)

    # 1:N 관계 설정
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    body = Column(String)

    # N:1 관계 설정
    post = relationship("Post", back_populates="comments")


def get_memory_usage():
    """현재 프로세스의 메모리 사용량을 MB 단위로 반환"""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


async def perform_random_crud_operations(session: AsyncSession, num_operations: int = 10000):
    """랜덤한 CRUD 작업을 수행하고 메모리 사용량을 측정"""

    start_memory = get_memory_usage()
    print(f"Initial memory usage: {start_memory:.2f} MB")

    for i in range(num_operations):
        operation = random.choice(["create", "read", "update", "delete"])

        if operation == "create":
            # Create
            post = Post(title=f"Post {i}", body=f"Body {i}")
            session.add(post)
            await session.commit()

            # Add 1-3 comments for each post
            num_comments = random.randint(1, 3)
            for j in range(num_comments):
                comment = Comment(post_id=post.id, body=f"Comment {j} for Post {i}")
                session.add(comment)
            await session.commit()

        elif operation == "read":
            # Read
            result = await session.execute("SELECT COUNT(*) FROM posts")
            count = result.scalar()
            if count > 0:
                post_id = random.randint(1, max(1, count))
                result = await session.execute(f"SELECT * FROM posts WHERE id = {post_id}")
                post = result.first()
                if post:
                    comments_result = await session.execute(f"SELECT * FROM comments WHERE post_id = {post_id}")
                    _ = comments_result.fetchall()

        elif operation == "update":
            # Update
            result = await session.execute("SELECT COUNT(*) FROM posts")
            count = result.scalar()
            if count > 0:
                post_id = random.randint(1, max(1, count))
                await session.execute(
                    f"UPDATE posts SET title = 'Updated Post {i}', body = 'Updated Body {i}' WHERE id = {post_id}"
                )
                await session.commit()

        else:  # delete
            # Delete
            result = await session.execute("SELECT COUNT(*) FROM posts")
            count = result.scalar()
            if count > 0:
                post_id = random.randint(1, max(1, count))
                await session.execute(f"DELETE FROM posts WHERE id = {post_id}")
                await session.commit()

        if (i + 1) % 1000 == 0:
            print(f"Completed {i + 1} operations")

    end_memory = get_memory_usage()
    print(f"Final memory usage: {end_memory:.2f} MB")
    print(f"Memory difference: {end_memory - start_memory:.2f} MB")


async def main():
    # DB 엔진 생성
    engine = create_async_engine("sqlite+aiosqlite:///test.db", echo=False)

    # 테이블 생성을 위한 임시 동기 엔진
    sync_engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(sync_engine)

    # 비동기 세션 생성
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        await perform_random_crud_operations(session=session, num_operations=100000)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
    # Initial memory usage: 37.66 MB.
    # After 10,000 operations, Final memory usage: 42.79 MB. diff: 5.13 MB
