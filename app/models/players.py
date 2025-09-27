from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Players(Base):
    __tablename__ = "players"

    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
