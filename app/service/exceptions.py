from fastapi import status


class BaseAPIException(Exception):
    """
    Base class for all API service exceptions.
    """

    status_code: int
    message: str

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message


class NotFoundException(BaseAPIException):
    def __init__(self, message: str) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, message)
