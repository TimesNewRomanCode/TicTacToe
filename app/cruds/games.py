from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.games import Games

class GamesCRUD:
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
        await session.commit()
        return result.rowcount

    async def update_game_winner(self, sid, winner_sid, session: AsyncSession):
        stmt = update(Games).where(Games.sid == sid).values(winner_sid=winner_sid)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount

    async def update_current_turn(self, sid, current_turn_sid, session: AsyncSession):
        stmt = update(Games).where(Games.sid == sid).values(current_turn_sid=current_turn_sid)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount