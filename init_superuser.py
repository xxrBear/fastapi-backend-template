from sqlmodel import Session, SQLModel, create_engine, select

from apps.core.security import get_password_hash
from apps.core.settings import settings
from apps.crud import user as crud_user
from apps.models import User, UserRegister

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)


def init_superuser(session: Session) -> None:
    user = session.exec(
        select(User).where(User.user_account == str(settings.FIRST_SUPERUSER))
    ).first()
    if not user:
        user_in = UserRegister(
            user_account=settings.FIRST_SUPERUSER,
            password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            is_superuser=True,
        )
        user = crud_user.create_user(session=session, user_in=user_in)


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    # init_superuser(session)
