from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.games import Games

class PlayersCRUD:
    def __init__(self):
        pass

    async def create_game(self, games: Games, session: AsyncSession):
        session.add(games)
        await session.commit()
        await session.refresh(games)

    async def list_games(self, session: AsyncSession):
        result = await session.execute(select(Games))
        return result.scalars().all()

    async def get_game_by_id(self, sid, session: AsyncSession):
        result = await session.execute(select(Games).where(Games.sid == sid))
        return result.scalars().one()

    async def update_game_status(self, sid, new_status, session: AsyncSession):
        stmt = update(Games).where(Games.sid == sid).values(status=new_status)
        result = await session.execute(stmt)
        return result.rowcount
