from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine, delete

from main import app
from models import User

TEST_DATABASE_URL = "postgresql://fast-admin:123456@localhost:5432/test"

engine = create_engine(TEST_DATABASE_URL)


# 初始化数据库表
def init_db_and_superuser():
    # 检查是否已经有表，避免重复创建
    SQLModel.metadata.create_all(engine)


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db_and_superuser()

        yield session
        statement = delete(User)
        session.execute(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


if __name__ == '__main__':
    init_db_and_superuser()
