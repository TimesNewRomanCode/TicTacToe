from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.moves import Moves

class PlayersCRUD:
    def __init__(self):
        pass

    async def create_move(self, moves: Moves, session: AsyncSession):
        session.add(moves)
        await session.commit()
        await session.refresh(moves)

    async def get_moves_by_game(self, game_sid, session: AsyncSession):
        result = await session.execute(select(Moves).where(Moves.game_sid == game_sid))
        return result.scalars().one()