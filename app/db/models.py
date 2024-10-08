from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True)
    fen = Column(String, nullable=False)
    eval = Column(Float)
    games = relationship("Game", secondary="game_position", back_populates="positions")


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    opening = Column(String)
    positions = relationship(
        "Position", secondary="game_position", back_populates="games"
    )


class GamePosition(Base):
    __tablename__ = "game_position"

    game_id = Column(Integer, ForeignKey("game.id"), primary_key=True)
    position_id = Column(Integer, ForeignKey("position.id"), primary_key=True)
