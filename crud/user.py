from sqlmodel import Session, select

from apps.models import User, UserRegister
from core.security import get_password_hash, verify_password


def authenticate(*, session: Session, user_account: str, password: str) -> User | None:
    """验证用户账号是否存在, 用户密码是否正确"""
    db_user = get_user_by_account(session=session, user_account=user_account)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user


def get_user_by_account(*, session: Session, user_account: str):
    """通过 user_account 查找用户"""
    statement = select(User).where(User.user_account == user_account)
    user_obj = session.exec(statement).first()
    return user_obj


def create_user(*, session: Session, user_in: UserRegister) -> User:
    """创建用户"""
    db_obj = User.model_validate(
        user_in, update={"hashed_password": get_password_hash(user_in.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj
