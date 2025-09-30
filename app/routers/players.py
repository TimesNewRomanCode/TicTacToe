from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.players import (
    RegistrationScheme,
    LoginScheme,
)
from app.services.players import PlayersService

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/registration")
async def registration(
    data: RegistrationScheme,
    session: AsyncSession = Depends(get_session),
    service: PlayersService = Depends(PlayersService),
):
    return await service.registration(data, session)


@router.post("/login")
async def login(
    data: LoginScheme,
    session: AsyncSession = Depends(get_session),
    service: PlayersService = Depends(PlayersService),
):
    return await service.login(data, session)

