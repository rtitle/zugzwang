from app.service.game_service import GameService
from app.service.position_service import PositionService


def get_game_service() -> GameService:
    return GameService()


def get_position_service() -> PositionService:
    return PositionService()
