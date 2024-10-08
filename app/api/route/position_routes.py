from typing import Any

from fastapi import APIRouter, Depends

from app.api import dependencies
from app.api.schema.position_schemas import Position
from app.service.position_service import PositionService

router = APIRouter()


@router.get("/{game_id}", response_model=list[Position])
async def enumerate_positions(
    game_id: int,
    skip: int = 0,
    limit: int = 100,
    position_service: PositionService = Depends(dependencies.get_position_service),
) -> Any:
    """
    Enumerates chess positions with the provided filters.

    :param game_id: the Game id.
    :param skip: number of records to offset.
    :param limit: limit results to the provided value.
    :param position_service: injected PositionService dependency.

    :return List of positions.
    :raise 404 error if the provided game was not found.
    """
    return await position_service.enumerate_positions(
        game_id=game_id, skip=skip, limit=limit
    )
