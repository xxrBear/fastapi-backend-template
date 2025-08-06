from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine, delete

from apps.models.user import User
from main import app

TEST_DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/mydb"

engine = create_engine(TEST_DATABASE_URL)


# 初始化数据库表
def init_db_and_superuser():
    # 检查是否已经有表，避免重复创建
    SQLModel.metadata.create_all(engine)


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        statement = delete(User)
        session.exec(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


if __name__ == "__main__":
    init_db_and_superuser()
