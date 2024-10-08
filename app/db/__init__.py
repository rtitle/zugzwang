from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy_repr import RepresentableBase

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./zugzwang.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_async_engine(
    # connect_args only needed for sqllite
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

global_sessionmaker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(cls=RepresentableBase)
