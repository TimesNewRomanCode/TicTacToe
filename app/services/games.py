from sqlalchemy.ext.asyncio import AsyncSession
from app.cruds.games import GamesCRUD
from app.models.games import Games, GameStatus
from app.schemas.games import StartGameScheme, GameStateRequest, FinishGameScheme


class GamesService:
    def __init__(self):
        self.games_crud = GamesCRUD()

    async def start_game(self, data: StartGameScheme, session: AsyncSession):
        new_game = Games(
            player1_sid=data.player1_sid,
            player2_sid=data.player2_sid,
            status=GameStatus.active,
            winner_sid=None,
            current_turn_sid=data.player1_sid
        )
        return await self.games_crud.create_game(new_game, session)

    async def game_info(self, session: AsyncSession):
        return await self.games_crud.list_games(session)

