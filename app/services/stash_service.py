from sqlalchemy import select
from app.extensions import db
from app.models import Stash

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