import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_account: str = Field(..., max_length=32, description="账号")

    username: str = Field(
        default="", max_length=32, description="用户昵称", nullable=True
    )
    user_avatar: str = Field(
        default="", max_length=64, description="用户头像", nullable=True
    )
    user_profile: str = Field(
        default="", max_length=512, description="用户简介", nullable=True
    )
    user_role: str = Field(
        default="user", max_length=32, description="用户角色：user/admin/ban"
    )
    create_time: datetime = Field(default_factory=datetime.now, description="创建时间")
    update_time: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
        description="更新时间",
    )
    is_active: bool = Field(default=False, description="是否删除", nullable=True)


class User(UserBase, table=True):
    """用户表"""

    __tablename__ = "users"

    hashed_password: str = Field(min_length=32, description="加密后的密码")
    is_superuser: bool = Field(default=False, description="是否超级管理员")


class UserPublic(UserBase):
    id: uuid.UUID


class UserRegister(SQLModel):
    username: str = Field(
        default="", max_length=32, description="用户昵称", nullable=True
    )
    password: str = Field(..., max_length=128, description="密码")
    user_account: str = Field(..., max_length=32, description="账号")


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None
