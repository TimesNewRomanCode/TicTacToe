from fastapi import APIRouter
from .players import router as players_router
from .games import router as games_router
from .moves import router as moves_router
router = APIRouter(prefix="/api")

router.include_router(players_router)
router.include_router(games_router)
router.include_router(moves_router)