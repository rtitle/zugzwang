from typing import Any

from sqlalchemy.orm import Session

from app.core import models
from app.core.db import SessionLocal, engine

# TODO: replace with alembic
models.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
