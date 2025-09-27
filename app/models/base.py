import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from datetime import datetime

class SIDMixin:
    sid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        nullable=False,
    )

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(default=func.now(), nullable=False)

class Base(DeclarativeBase, SIDMixin):
    pass
