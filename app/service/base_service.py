from app.db import db_session_maker


class BaseService:
    """
    Base service class containing common infrastructure for services.
    """

    def __init__(self):
        self.db_session_maker = db_session_maker
