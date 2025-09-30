from uuid import UUID

from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from .base import Base


class Moves(Base):
    __tablename__ = "moves"

    game_sid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("games.sid"), nullable=False)
    player_sid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("players.sid"), nullable=False)
    position_x: Mapped[int] = mapped_column(Integer, nullable=False)
    position_y: Mapped[int] = mapped_column(Integer, nullable=False)
    value: Mapped[bool] = mapped_column(Boolean)

