from fastapi import APIRouter

from app.api.routes import positions, utils

api_router = APIRouter()
api_router.include_router(positions.router, prefix="/positions/v1", tags=["positions"])
api_router.include_router(utils.router, tags=[])
