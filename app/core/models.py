from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True)
    fen = Column(String, nullable=False)
    eval = Column(Float)
    games = relationship("Game", secondary="game_position", backref="position")


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    opening = Column(String)
    positions = relationship("Position", secondary="game_position", backref="game")


class GamePosition(Base):
    __tablename__ = "game_position"

    game_id = Column(Integer, ForeignKey("game.id"), primary_key=True)
    position_id = Column(Integer, ForeignKey("position.id"), primary_key=True)
    move_number = Column(Integer, nullable=False)
    move_color = Column(String, nullable=False)
    move = Column(String, nullable=False)
