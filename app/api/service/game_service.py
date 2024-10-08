import aiofiles
import chess.pgn
from sqlalchemy.orm import Session

from app.api.service import position_service
from app.db import models


class GameService:
    # TODO error handling if game not found
    def get_game(self, db: Session, game_id: int) -> models.Game:
        """
        Gets a game by ID.

        :param db: database session.
        :param game_id: the game ID to look up.

        :return Game DB model object.
        """
        return db.query(models.Game).where(models.Game.id == game_id).first()

    # TODO error handling
    # TODO async?
    async def import_pgn(self, db: Session, filename: str, content: bytes) -> None:
        """
        Imports a PGN file to the database.

        :param db: database session.
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
        db.add(db_game)
        db.commit()
