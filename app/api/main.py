from fastapi import APIRouter

from app.api.routes import games, utils

api_router = APIRouter()
api_router.include_router(games.router, prefix="/games", tags=["games"])
api_router.include_router(utils.router, tags=[])
