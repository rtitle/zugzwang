from sqlalchemy.future import select

from app.db import models
from app.service.base_service import BaseService
from app.service.exceptions import NotFoundException
from fastapi_cache.decorator import cache


class PositionService(BaseService):
    async def enumerate_positions(
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
        async with self.sessionmaker() as session:
            # raise 404 if the game does not exist
            exists_query = select(models.Game.id).where(models.Game.id == game_id)
            result = await session.execute(exists_query)
            game_exists = result.scalar()
            if not game_exists:
                raise NotFoundException("Game not found")

            position_query = (
                select(models.Position)
                .join(models.GamePosition)
                .join(models.Game)
                .filter(models.Game.id == game_id)
                .offset(skip)
                .limit(limit)
            )
            result = await session.execute(position_query)
            return result.scalars()
    
    @cache(expire=60)
    async def evaluate_position(self, fen: str) -> float:
        """
        Evaluates a chess position.
        Caches results since evaluation can be expensive.
        Note: it might make more sense to store the evaluations in the database,
        since they do not change. But I wanted to practice using a caching library.

        :param fen: the FEN representation of the position.
        
        :return the evaluation as a float.
        """

        # TODO implement evaluation
        return 1.2

