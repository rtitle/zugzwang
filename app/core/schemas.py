from typing import Optional

from pydantic import BaseModel


class GameBase(BaseModel):
    white: str
    black: str
    white_elo: int
    black_elo: int
    opening: Optional[str]


class Game(GameBase):
    pass


class GameCreate(GameBase):
    pass
