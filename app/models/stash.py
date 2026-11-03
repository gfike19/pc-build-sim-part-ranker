from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db

class Stash (db.Model):
    __tablename__ = "stashes"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    parts: Mapped[list["Part"]] = relationship(
        back_populates="container",
        cascade="all, delete-orphan"
    )
