from sqlalchemy import select
from app.extensions import db
from app.models import Part


def get_all_parts() -> list[Part]:
    parts = db.session.scalars(select(Part).order_by(Part.partScore)).all()
    return parts

def get_all_cpus() -> list[Part]:
    parts = db.session.scalars(select(Part).where(Part.cpu == True)).all()
    return parts

def get_all_gpus() -> list[Part]:
    parts = db.session.scalars(select(Part).where(Part.gpu == True)).all()
    return parts

# underscore in _in is used to differentiate between python and sql keywords
def get_parts_by_ids(part_ids: list[int]) -> list[Part]:
    return db.session.scalars(select(Part).where(Part.id.in_(part_ids))).all()