from sqlalchemy.ext.asyncio import AsyncSession
from app.cruds.players import PlayersCRUD
from app.models.players import Players
from app.schemas.players import RegistrationScheme, LoginScheme


class PlayersService:
    def __init__(self):
        self.player_crud = PlayersCRUD()

    async def registration(self, data: RegistrationScheme, session: AsyncSession):
        existing_player = await self.player_crud.get_player_by_username(data.username, session)
        if existing_player:
            return None

        new_player = Players(
            username=data.username,
            password=data.password,
        )

        return await self.player_crud.create_players(new_player, session)

    async def login(self, data: LoginScheme, session: AsyncSession):
        player = await self.player_crud.get_player_by_username(data.username, session)
        if not player:
            return None

        if data.password != player.password:
            return None

        return player