from typing import Optional

from pydantic import BaseModel, Field


class Game(BaseModel):
    """
    Base representation of a chess game.

    :param id: identifier of the game.
    :param description: user-friendly description of the game.
    :param opening: annotated opening of the game.
    """

    id: int = Field(example=1)
    description: str = Field(examples=["Rated event"])
    opening: Optional[str] = Field(
        examples=["French Defense: Advance Variation, Nimzowitsch System"], default=None
    )
