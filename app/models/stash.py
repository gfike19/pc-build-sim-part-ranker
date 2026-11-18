from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db
from .associations import stash_parts

if TYPE_CHECKING:
    from .part import Part


class Stash(db.Model):
    __tablename__ = "stashes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    stashName: Mapped[String] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    parts: Mapped[list["Part"]] = relationship(
        secondary=stash_parts,
        back_populates="stashes"
    )