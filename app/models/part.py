from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db


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

    # Foreign key to Stash
    stash_id: Mapped[int | None] = mapped_column(
        ForeignKey("stashes.id"),
        nullable=True
    )

    # Relationship
    container: Mapped["Stash | None"] = relationship(
        back_populates="parts"
    )
