from fastapi import APIRouter
from .players import router as players_router

router = APIRouter(prefix="/api")

router.include_router(players_router)

