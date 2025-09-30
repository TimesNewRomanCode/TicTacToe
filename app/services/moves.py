from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from app.cruds.moves import MovesCRUD
from app.cruds.games import GamesCRUD
from app.models import Moves
from app.models.games import Games, GameStatus
from app.schemas.moves import MovesScheme, MakeMoveScheme, CheckWinnerRequest


class MovesService:
    def __init__(self):
        self.moves_crud = MovesCRUD()
        self.games_crud = GamesCRUD()

    async def game_info(self, data:MovesScheme, session: AsyncSession):
        return await self.moves_crud.get_moves_by_game(data.sid, session)

    async def make_move(self, data: MakeMoveScheme, session: AsyncSession):
        # Валидация координат
        if not (0 <= data.position_x <= 2 and 0 <= data.position_y <= 2):
            raise ValueError("Coordinates must be between 0 and 2")

        game = await self.games_crud.get_game_by_id(data.game_sid, session)

        if game.status != GameStatus.active:
            raise ValueError("Game is not active")

        if game.current_turn_sid != data.player_sid:
            raise ValueError("Not your turn")

        existing_move = await self.moves_crud.get_move_by_position(
            data.game_sid, data.position_x, data.position_y, session
        )
        if existing_move:
            raise ValueError("Cell is already occupied")

        new_move = Moves(
            game_sid=data.game_sid,
            player_sid=data.player_sid,
            position_x=data.position_x,
            position_y=data.position_y,
            value=True if data.player_sid == game.player1_sid else False
        )
        await self.moves_crud.create_move(new_move, session)

        winner = await self.check_winner(data.game_sid, session)
        if winner:
            await self.games_crud.update_game_status(
                data.game_sid, GameStatus.finished, session
            )
            await self.games_crud.update_game_winner(
                data.game_sid, winner, session
            )
        else:
            next_player = game.player2_sid if data.player_sid == game.player1_sid else game.player1_sid
            await self.games_crud.update_current_turn(
                data.game_sid, next_player, session
            )
            await session.commit()



    async def check_winner(self, game_sid: UUID, session: AsyncSession) -> UUID | None:
        moves = await self.moves_crud.get_moves_by_game(game_sid, session)

        board = [[None for _ in range(3)] for _ in range(3)]
        for move in moves:
            symbol = 'O' if move.value else 'X'
            board[move.position_y][move.position_x] = (symbol, move.player_sid)

        for i in range(3):
            cell1 = board[i][0]
            cell2 = board[i][1]
            cell3 = board[i][2]
            if cell1 and cell2 and cell3 and cell1[0] == cell2[0] == cell3[0]:
                return cell1[1]

            cell1 = board[0][i]
            cell2 = board[1][i]
            cell3 = board[2][i]
            if cell1 and cell2 and cell3 and cell1[0] == cell2[0] == cell3[0]:
                return cell1[1]

        cell1 = board[0][0]
        cell2 = board[1][1]
        cell3 = board[2][2]
        if cell1 and cell2 and cell3 and cell1[0] == cell2[0] == cell3[0]:
            return cell1[1]

        cell1 = board[0][2]
        cell2 = board[1][1]
        cell3 = board[2][0]
        if cell1 and cell2 and cell3 and cell1[0] == cell2[0] == cell3[0]:
            return cell1[1]

        return None

    async def move_all(self, session: AsyncSession):
        return await self.moves_crud.get_moves(session)