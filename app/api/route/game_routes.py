from typing import Any

from fastapi import APIRouter, Depends, UploadFile

from app.api import dependencies
from app.api.schema.game_schemas import Game
from app.service.game_service import GameService

router = APIRouter()


@router.get("/{game_id}", response_model=Game)
async def get_game(
    game_id: int, game_service: GameService = Depends(dependencies.get_game_service)
) -> Any:
    """
    Gets a game by ID.

    :param game_id: the game ID.
    :param game_service: injected GameService dependency.

    :return a Game model.
    :raise 404 exception if the game does not exist.
    """
    return await game_service.get_game(game_id)


@router.put("/pgn", status_code=204)
async def import_pgn(
    in_file: UploadFile,
    game_service: GameService = Depends(dependencies.get_game_service),
) -> None:
    """
    Imports games from a PGN file.

    :param in_file: uploaded PGN file.
    :param game_service: injected GameService dependency.

    :return 204 status with no content.
    """
    content = await in_file.read()
    await game_service.import_pgn(in_file.filename, content)
