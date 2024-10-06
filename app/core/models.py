from sqlalchemy import Column, Integer, String

from app.core.db import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    white = Column(String, nullable=False)
    black = Column(String, nullable=False)
    white_elo = Column(Integer, nullable=False)
    black_elo = Column(Integer, nullable=False)
    opening = Column(String)
