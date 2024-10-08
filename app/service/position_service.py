from app.db import models
from app.service.base_service import BaseService
from app.service.exceptions import NotFoundException


class PositionService(BaseService):
    def enumerate_positions(
        self, game_id: int, skip: int, limit: int
    ) -> list[models.Position]:
        """
        Enumerates chess positions for a given game.

        :param game_id: the game id to retrieve positions for,
        :param skip: the offset for the database query. Default 0.
        :param limit: the limit for the database query. Default 100.

        :return list of Position objects.
        :raise NotFoundException if the game does not exist.
        """
        with self.db_session_maker() as session:
            # raise 404 if the game does not exist
            game_exists = (
                session.query(models.Game.id).where(models.Game.id == game_id).first()
            )
            if not game_exists:
                raise NotFoundException("Game not found")

            return (
                session.query(models.Position)
                .join(models.GamePosition)
                .join(models.Game)
                .filter(models.Game.id == game_id)
                .offset(skip)
                .limit(limit)
            )
