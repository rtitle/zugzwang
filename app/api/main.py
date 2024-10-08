from fastapi import APIRouter

from app.api.route import game_routes, position_routes, util_routes

api_router = APIRouter()
api_router.include_router(
    position_routes.router, prefix="/positions/v1", tags=["positions"]
)
api_router.include_router(game_routes.router, prefix="/games/v1", tags=["games"])
api_router.include_router(util_routes.router, tags=[])
