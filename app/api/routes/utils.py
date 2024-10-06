from typing import Any

from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
async def docs_redirect() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/health-check/")
async def health_check() -> bool:
    return True
