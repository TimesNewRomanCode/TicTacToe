import enum
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy import Column, DateTime, ForeignKey, Enum
from sqlalchemy.sql.sqltypes import String
from app.models.base import Base


class GameStatus(enum.Enum):
    waiting = "waiting"
    active = "active"
    finished = "finished"


class Games(Base):
    __tablename__ = "games"

    player1_sid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("players.sid"), nullable=False)
    player2_sid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("players.sid"), nullable=False)
    board_player1: Mapped[str] = mapped_column(String, nullable=False)
    board_player2: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[GameStatus] = mapped_column(Enum(GameStatus), default=GameStatus.waiting, nullable=False)
    winner_sid: Mapped[Optional[UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("players.sid"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    current_turn_sid: Mapped[Optional[UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("players.sid"), nullable=True)