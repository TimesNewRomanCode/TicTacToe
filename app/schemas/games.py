from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class StartGameScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    player1_sid: UUID
    player2_sid: UUID


class GameInfoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    games_sid: UUID
    player1_sid: UUID
    player2_sid: Optional[UUID]
    board: str
    status: str
    winner_sid: Optional[UUID]
    current_turn_sid: Optional[UUID]


class MakeMoveScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_sid: UUID
    player_sid: UUID
    position: int


class GameStateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_sid: UUID


class GameStateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    winner: Optional[str]
    is_draw: bool
    is_finished: bool


class FinishGameScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_sid: UUID
    winner_sid: Optional[UUID] = None