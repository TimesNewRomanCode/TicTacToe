from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID

class MovesScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sid: UUID


class MakeMoveScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_sid: UUID
    player_sid: UUID
    position_x: int = Field(ge=0, le=2)  # 0-2
    position_y: int = Field(ge=0, le=2)  # 0-2

class CheckWinnerRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    game_sid: UUID