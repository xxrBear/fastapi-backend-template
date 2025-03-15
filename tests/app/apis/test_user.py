from fastapi.testclient import TestClient
from sqlmodel import Session

from crud import user as user_crud
from models import UserRegister


def test_create_user(client: TestClient, db: Session) -> None:
    user_account = "xxx"
    password = "xxx"
    user_info = UserRegister(**{"user_account": user_account, "password": password})
    user = user_crud.create_user(session=db, user_in=user_info)

    assert user_account == user.user_account
    assert hasattr(user, "hashed_password")
