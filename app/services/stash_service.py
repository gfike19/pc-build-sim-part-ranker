from sqlalchemy import select
from app.extensions import db
from app.models import Stash, Part

def create_new_stash(stashName: str) -> Stash:
    name = stashName.strip()
    if not name:
        raise ValueError("Stash name cannot be empty")
    stash = Stash(stashName=name)
    
    try:
        db.session.add(stash)
        db.session.commit()
    except IndexError:
        db.session.rollback()
        raise

    return stash

def get_all_Stashes() -> list[Stash]:
    stashes = db.session.scalars(select(Stash).order_by(Stash.id)).all()
    return stashes

def get_stash_by_id(id: int) -> Stash:
    stash = db.session.get(Stash, id)
    if stash is None:
        raise ValueError(f"Stash with ID {id} does not exist.")
    else:
        return stash

def del_stash_by_id(id: int) -> Stash:
    stash = get_stash_by_id(id)
    db.session.delete(stash)
    db.session.commit()

def add_parts(stash_id, part_ids):
    stash = get_stash_by_id(stash_id)
    parts = db.session.scalars(db.select(Part).where(Part.id.in_(part_ids))).all()
    stash.parts.extend(parts)
    db.session.commit()