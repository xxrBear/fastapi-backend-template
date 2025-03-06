from typing import Any

from fastapi.routing import APIRouter

from app.deps import SessionDep
from crud import user as user_crud
from models import UserRegister

router = APIRouter(tags=["user"])


@router.post("/signup")
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
