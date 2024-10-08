from typing import Optional

from pydantic import BaseModel


# todo add some examples
class Position(BaseModel):
    """
    A chess position.

    :param game_id: identifier of the game this position belongs to.
    :param fen: FEN notation of the position.
    :param eval: evaluation of the position, if calculated.
    :param move_number: the move number in the game.
    :param move_color: the move color in the game.
    :param move: the move in PGN format.
    """

    game_id: int
    fen: str
    eval: Optional[float]
    move_number: int
    move_color: str
    move: str
