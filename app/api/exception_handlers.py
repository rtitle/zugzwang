from fastapi import Request
from starlette.responses import JSONResponse

from app.api.schema.error_schemas import BaseAPIError
from app.service.exceptions import BaseAPIException


async def http_exception_handler(_: Request, exc: BaseAPIException) -> JSONResponse:
    content = BaseAPIError(status=exc.status_code, message=exc.message).model_dump(
        mode="json"
    )
    return JSONResponse(content, status_code=exc.status_code)
