from sqlalchemy.orm import Session

from app.core import models, schemas


def get_game(db: Session, game_id: int) -> models.Game:
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_games(db: Session, skip: int = 0, limit: int = 100) -> list[models.Game]:
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_game(db: Session, game: schemas.GameCreate) -> models.Game:
    db_game = models.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
