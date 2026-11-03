from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db

class Part (db.Model):
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

    container: Mapped["Stash"] = relationship(
        back_populates="parts"
    )
