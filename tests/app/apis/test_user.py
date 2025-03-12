from fastapi.testclient import TestClient
from sqlmodel import Session


def test_create_user_new_account(client: TestClient, db: Session) -> None:
    user_account = "xxx"
    password = "xxx"
    data = {"user_account": user_account, "password": password}
    r = client.post(
        "api/user/signup",
        json=data,
    )
    assert r.status_code == 200
    created_user = r.json()
    assert user_account == created_user["user_account"]
