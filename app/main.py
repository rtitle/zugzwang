from fastapi import APIRouter, FastAPI

from app.api.exception_handlers import http_exception_handler
from app.api.route import game_routes, position_routes, util_routes
from app.api.schema.error_schemas import NotFoundError
from app.service.exceptions import BaseAPIException

api_router = APIRouter()
api_router.include_router(
    position_routes.router, prefix="/positions/v1", tags=["positions"]
)
api_router.include_router(game_routes.router, prefix="/games/v1", tags=["games"])
api_router.include_router(util_routes.router, tags=[])


app = FastAPI(title="Project Zugzwang")
app.include_router(api_router, responses={404: {"model": NotFoundError}})

app.add_exception_handler(BaseAPIException, http_exception_handler)
