from typing import Optional

from pydantic import BaseModel


class Position(BaseModel):
    """
    A chess position.

    :param game_id: identifier of the game this position belongs to.
    :param fen: FEN notation of the position.
    :param eval: evaluation of the position, if calculated.
    """

    fen: str
    eval: float | None = None


class Game(BaseModel):
    """
    Base representation of a chess game.

    :param id: identifier of the game.
    :param description: user-friendly description of the game.
    :param opening: annotated opening of the game.
    """

    id: int
    description: str
    opening: str | None = None
