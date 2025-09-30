from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.games import StartGameScheme, GameStateRequest

from app.services.games import GamesService

router = APIRouter(prefix="/games", tags=["games"])


@router.post("/games/sid/sid")
async def start_game(
    data: StartGameScheme,
    session: AsyncSession = Depends(get_session),
    service: GamesService = Depends(GamesService),
):
    return await service.start_game(data, session)

@router.get("/games")
async def game_info(
    session: AsyncSession = Depends(get_session),
    service: GamesService = Depends(GamesService),
):
    return await service.game_info(session)


