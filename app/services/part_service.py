from sqlalchemy import select

from app.extensions import db
from app.models import Stash


def get_user_by_email(email: str) -> User | None:

    stmt = select(User).where(
        User.email == email
    )

    return db.session.scalar(stmt)


def create_user(name: str, email: str) -> User:

    user = User(
        name=name,
        email=email
    )

    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    return user
