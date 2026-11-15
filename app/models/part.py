from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db
from .associations import stash_parts

if TYPE_CHECKING:
    from .stash import Stash


class Part(db.Model):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    partName: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    partScore: Mapped[int] = mapped_column(
        nullable=False
    )

    gpu: Mapped[bool] = mapped_column(
        nullable=False
    )

    cpu: Mapped[bool] = mapped_column(
        nullable=False
    )

    stashes: Mapped[list["Stash"]] = relationship(
        secondary=stash_parts,
        back_populates="parts"
    )