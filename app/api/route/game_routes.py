from typing import Any

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from app.api import dependencies, schemas
from app.api.service import game_service

router = APIRouter()


@router.get("/{game_id}", response_model=schemas.Game)
def get_game(game_id: int, db: Session = Depends(dependencies.get_db)) -> Any:
    """
    Gets a game by ID.
    """
    return game_service.get_game(db, game_id)


@router.put("/pgn", status_code=204)
async def import_pgn(
    in_file: UploadFile, db: Session = Depends(dependencies.get_db)
) -> None:
    """
    Imports games from a PGN file.
    """
    content = await in_file.read()
    await game_service.import_pgn(db, in_file.filename, content)
