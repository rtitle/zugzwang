from sqlalchemy.orm import Session

from app.core import models, schemas


def enumerate_positions(
    db: Session, skip: int = 0, limit: int = 100, game_ids: list[int] = []
) -> list[models.Position]:
    """
    Enumerates chess positions with the provided filters.

    :param db: the database session.
    :param skip: the offset for the database query. Default 0.
    :param limit: the limit for the database query. Default 100.
    :param game_ids: filter to the provided game ids. Defaut to no filter.

    :return list of Position objects.
    """
    base = (
        db.query(models.Position, models.Game, models.GamePosition)
        .filter(models.Position.id == models.GamePosition.position_id)
        .filter(models.Game.id == models.GamePosition.game_id)
    )

    with_game_filter = base.filter(models.Game.id.in_(game_ids)) if game_ids else base

    return with_game_filter.offset(skip).limit(limit)
