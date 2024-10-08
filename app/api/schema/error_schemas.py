from fastapi import status
from pydantic import BaseModel, Field


class BaseAPIError(BaseModel):
    """
    Base API error model containing a status code and a message.

    :param status: HTTP status code.
    :param message: message string.
    """

    status: int
    message: str


class NotFoundError(BaseAPIError):
    status: int = Field(example=status.HTTP_404_NOT_FOUND)
    message: str = Field(example="Game not found")
