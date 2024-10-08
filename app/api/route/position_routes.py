from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import dependencies, schemas
from app.api.service import position_service

router = APIRouter()


@router.get("/{game_id}", response_model=list[schemas.Position])
def enumerate_positions(
    game_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(dependencies.get_db),
) -> Any:
    """
    Enumerates chess positions with the provided filters.

    :param skip: number of records to offset.
    :param limit: limit results to the provided value.
    :param game_ids: limit results to the provided game IDs.

    :return List of positions.
    """
    db_positions = position_service.enumerate_positions(
        db, game_id=game_id, skip=skip, limit=limit
    )
    return db_positions
