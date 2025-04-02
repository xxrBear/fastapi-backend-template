from typing import Any

from fastapi import APIRouter

from apps.crud import user as user_crud
from apps.deps import SessionDep
from apps.models import UserRegister
from apps.models.user import UserPublic

router = APIRouter(tags=["user"])


@router.post("/signup", response_model=UserPublic)
def register_user(session: SessionDep, user_in: UserRegister) -> Any:
    """
    register user
    """
    user_obj = user_crud.get_user_by_account(
        session=session, user_account=user_in.user_account
    )
    if user_obj:
        pass
    user = user_crud.create_user(session=session, user_in=user_in)
    return user
