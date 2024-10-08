from typing import Any

from sqlalchemy.orm import Session

from app.core import models
from app.core.db import SessionLocal, engine


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
