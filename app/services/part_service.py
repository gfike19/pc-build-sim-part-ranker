from sqlalchemy import select
from app.extensions import db
from app.models import Part


def get_all_parts() -> list[Part]:
    parts = db.session.scalars(select(Part).order_by(Part.partScore)).all()
    return parts
