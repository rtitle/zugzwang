import aiofiles
import chess.pgn
from sqlalchemy.future import select

from app.db import models
from app.service.base_service import BaseService
from app.service.exceptions import NotFoundException


class GameService(BaseService):
    async def get_game(self, game_id: int) -> models.Game:
        """
        Gets a game by ID.

        :param game_id: the game ID to look up.

        :return Game DB model object.
        :raise NotFoundException if the game does not exist.
        """
        async with self.sessionmaker() as session:
            query = select(models.Game).where(models.Game.id == game_id)
            result = await session.execute(query)
            game = result.scalar()
            if not game:
                raise NotFoundException("Game not found")
            return game

    async def import_pgn(self, filename: str, content: bytes) -> None:
        """
        Imports a PGN file to the database.

        :param filename: name of the uploaded PGN file.
        :param content: content in bytes of the PGN file.
        """
        # Write the PGN file to disk
        out_file_name = f"files/{filename}"
        async with aiofiles.open(out_file_name, "wb") as out_file:
            await out_file.write(content)

        # Load the PGN file into the chess library.
        parsed_pgn = open(out_file_name)
        first_game = chess.pgn.read_game(parsed_pgn)

        # Read headers of the game and build the Game model.
        event = first_game.headers["Event"]
        opening = first_game.headers["Opening"]
        db_game = models.Game(description=event, opening=opening)

        # Iterate through positions of the game and build the Position models.
        # TODO: read more than the first game.
        db_positions = []
        board = first_game.board()
        for move in first_game.mainline_moves():
            board.push(move)
            db_position = models.Position(fen=board.fen())
            db_positions.append(db_position)

        db_game.positions.extend(db_positions)

        # Persist to the database.
        async with self.sessionmaker() as session:
            session.add(db_game)
            session.commit()
