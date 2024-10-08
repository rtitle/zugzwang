from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db import global_sessionmaker


class BaseService:
    """
    Base service class containing common infrastructure for services.
    """

    def __init__(self, sessionmaker: async_sessionmaker = global_sessionmaker) -> None:
        self.sessionmaker = sessionmaker
