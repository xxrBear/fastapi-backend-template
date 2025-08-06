from typing import Any

from fastapi import APIRouter

from apps.core.resp import render_json
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


@router.delete('/user')
def delete_user(session: SessionDep, user_id: str):
    user_obj = user_crud.get_user_by_id(session=session, user_id=user_id)
    if user_obj:
        session.delete(user_obj)
        session.commit()
        return render_json(message="删除成功！")
    else:
        return render_json(code=404, message="删除失败，用户不存在！")
