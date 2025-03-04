from datetime import datetime

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    id: int = Field(index=True, primary_key=True, description="用户id")
    user_account: str = Field(..., max_length=32, description="账号")
    union_id: str = Field(
        default="", max_length=256, description="微信开放平台id", nullable=True
    )
    mp_open_id: str = Field(
        default="", max_length=256, description="公众号openId", nullable=True
    )
    user_name: str = Field(
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
    is_delete: bool = Field(default=False, description="是否删除", nullable=True)


class User(UserBase, table=True):
    """用户表"""

    user_password: str = Field(..., max_length=64, description="密码")


class UserCreate(SQLModel):
    user_account: str = Field(min_length=4, max_length=32, description="账号")
    user_password: str = Field(min_length=8, max_length=64, description="密码")
    check_password: str = Field(min_length=8, max_length=64, description="检验密码")


class UserLogin(SQLModel):
    user_account: str = Field(min_length=4, max_length=32, description="账号")
    user_password: str = Field(min_length=8, max_length=32, description="密码")


class UserPage(SQLModel):
    current: int = Field(default=1, description="开始页")
    page_size: int = Field(default=10, description="总页数")
    username: str = Field(default="", description="用户名")
    user_desc: str = Field(default="", description="用户描述")
    user_profile: str = Field(default="", description="")


class UserDelete(SQLModel):
    id: int = Field(description="用户id")
