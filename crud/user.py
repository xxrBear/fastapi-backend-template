from sqlmodel import Session, select

from core.security import get_password_hash
from models import User, UserRegister


def get_user_by_account(*, session: Session, user_account: str):
    """通过 user_account 查找用户"""
    statement = select(User).where(User.user_account == user_account)
    user_obj = session.exec(statement).first()
    return user_obj


def create_user(*, session: Session, user_in: UserRegister) -> User:
    db_obj = User.model_validate(
        user_in, update={"hashed_password": get_password_hash(user_in.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj
