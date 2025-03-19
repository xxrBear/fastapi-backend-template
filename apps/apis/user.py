from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from apps.deps import CurrentUser, SessionDep
from apps.models import UserRegister
from apps.models.user import Token, User, UserPublic
from core.security import create_access_token
from crud import user as user_crud

router = APIRouter(tags=["user"])


@router.post("/signup", response_model=UserPublic)
def register_user(session: SessionDep, user_in: UserRegister) -> Any:
    """
    注册用户
    """
    user_obj = user_crud.get_user_by_account(
        session=session, user_account=user_in.user_account
    )
    if user_obj:
        pass
    user = user_crud.create_user(session=session, user_in=user_in)
    return user


@router.post("/login/test-token", response_model=User)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """
    return current_user


@router.post("/login/access-token")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 兼容的令牌登录，获取访问令牌以供后续请求使用
    """
    user = user_crud.authenticate(
        session=session, user_account=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=60 * 60 * 24)
    return Token(
        access_token=create_access_token(user.id, expires_delta=access_token_expires)
    )
