import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from .base import Base


class Players(Base):
    __tablename__ = 'players'
    sid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)