from typing import Optional

from pydantic import BaseModel, Field


class Position(BaseModel):
    """
    A chess position.

    :param game_id: identifier of the game this position belongs to.
    :param fen: FEN notation of the position.
    :param eval: evaluation of the position.
    """

    fen: str = Field(
        examples=["rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"]
    )
    eval: Optional[float] = Field(examples=["0.5"], default=None)
