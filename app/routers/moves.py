from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.moves import (
    MovesScheme, MakeMoveScheme,
)
from app.services.moves import MovesService

router = APIRouter(prefix="/moves", tags=["moves"])


@router.post("/games/{game_sid}/move")
async def game_info(
    data: MovesScheme,
    session: AsyncSession = Depends(get_session),
    service: MovesService = Depends(MovesService),
):
    return await service.game_info(data, session)

@router.post("/games/move")
async def make_move(
    data: MakeMoveScheme,
    session: AsyncSession = Depends(get_session),
    service: MovesService = Depends(MovesService),
):
    return await service.make_move(data, session)

@router.get("/games/moves")
async def move_all(
    session: AsyncSession = Depends(get_session),
    service: MovesService = Depends(MovesService),
):
    return await service.move_all(session)


