from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core import crud, schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Game])
def list_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    db_games = crud.get_games(db, skip=skip, limit=limit)
    return db_games


@router.get("/{game_id}", response_model=schemas.Game)
def get_game(game_id: int, db: Session = Depends(get_db)) -> Any:
    db_game = crud.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return db_game


@router.post("/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)) -> Any:
    return crud.create_game(db=db, game=game)
