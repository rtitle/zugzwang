from sqlalchemy.orm import Session

from app.db import models


class PositionService:
    def enumerate_positions(
        self, db: Session, game_id: int, skip: int, limit: int
    ) -> list[models.Position]:
        """
        Enumerates chess positions for a given game.

        :param db: the database session.
        :param game_id: the game id to retrieve positions for,
        :param skip: the offset for the database query. Default 0.
        :param limit: the limit for the database query. Default 100.

        :return list of Position objects.
        """
        # TODO: error handling if game not found
        q = (
            db.query(models.Position)
            .join(models.GamePosition)
            .join(models.Game)
            .filter(models.Game.id == game_id)
        )

        return q.offset(skip).limit(limit)
