from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from apps.crud import user as user_crud
from apps.models import UserRegister
from apps.tests.conftest import client


def test_create_user(client: TestClient, db: Session) -> None:
    user_account = "xxx"
    password = "xxx"
    user_info = UserRegister(**{"user_account": user_account, "password": password})
    user = user_crud.create_user(session=db, user_in=user_info)

    assert user_account == user.user_account
    assert hasattr(user, "hashed_password")


# 假设 user_crud 在 app.crud.user_crud 模块下
@pytest.fixture
def fake_user():
    class User:
        id = "123"
        name = "Test User"

    return User()


def test_delete_user_success(fake_user):
    with (
        patch("app.crud", return_value=fake_user) as mock_get_user,
        patch("app.api.SessionDep") as mock_session,
    ):
        mock_session_instance = mock_session.return_value
        mock_session_instance.delete.return_value = None
        mock_session_instance.commit.return_value = None

        response = client.delete(
            "/user", params={"user_id": "3ad911f5-bd82-4810-86f4-bf48f0053df1"}
        )

        assert response.status_code == 200
        assert response.json()["message"] == "删除成功！"
        mock_get_user.assert_called_once_with(
            session=mock_session_instance, user_id="123"
        )


def test_delete_user_not_found():
    with (
        patch("app.crud.get_user_by_id", return_value=None) as mock_get_user,
        patch("app.api.SessionDep") as mock_session,
    ):
        response = client.delete(
            "/user", params={"user_id": "3ad911f5-bd82-4810-86f4-bf48f0053df1"}
        )

        assert response.status_code == 200  # 因为 render_json 默认 http_status 是 200
        assert response.json()["code"] == 404
        assert response.json()["message"] == "删除失败，用户不存在！"
        mock_get_user.assert_called_once()
