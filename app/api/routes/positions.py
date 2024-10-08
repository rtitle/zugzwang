from typing import Any

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core import crud, schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Position])
def enumerate_positions(
    skip: int = 0,
    limit: int = 100,
    game_ids: list[int] = Query(None),
    db: Session = Depends(get_db),
) -> Any:
    """
    Enumerates chess positions with the provided filters.

    :param skip: number of records to offset.
    :param limit: limit results to the provided value.
    :param game_ids: limit results to the provided game IDs.

    :return List of positions.
    """
    db_positions = crud.enumerate_positions(
        db, skip=skip, limit=limit, game_ids=game_ids
    )
    return db_positions
