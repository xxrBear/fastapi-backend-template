from sqlmodel import SQLModel, create_engine

from models import User

# 使用 SQLAlchemy 的 SQLite URL 格式
DATABASE_URL = "postgresql://fast-admin:123456@localhost:5432/backend_tem"

engine = create_engine(DATABASE_URL, echo=True)


# 初始化数据库表
def init_db_and_superuser():
    # 检查是否已经有表，避免重复创建
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    init_db_and_superuser()
