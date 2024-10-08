from typing import Any

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/", include_in_schema=False)
async def docs_redirect() -> Any:
    """
    Redirects / to the Swagger docs page.
    """
    return RedirectResponse(url="/docs")


@router.get("/health-check/")
async def health_check() -> bool:
    """
    Endpoint for health checking.
    """
    return True
