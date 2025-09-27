from uuid import UUID

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from .base import Base


class Moves(Base):
    __tablename__ = "moves"

    game_sid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("games.sid"), nullable=False)
    player_sid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("players.sid"), nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=False)
