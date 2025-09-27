from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.players import Players

class PlayersCRUD:
    def __init__(self):
        pass

    async def create_players(self, players: Players, session: AsyncSession):
        session.add(players)
        await session.commit()
        await session.refresh(players)

    async def get_all_Players(self, session: AsyncSession):
        result = await session.execute(select(Players))
        return result.scalars().all()

    async def get_player_by_id(self, sid, session: AsyncSession):
        result = await session.execute(select(Players).where(Players.sid == sid))
        return result.scalars().one()

    async def get_player_by_username(self, username, session: AsyncSession):
        result = await session.execute(select(Players).where(Players.username == username))
        return result.scalars().first()

    async def delete_player(self, sid, session: AsyncSession):
        result = await session.execute(delete(Players).where(Players.sid == sid))
        return result

