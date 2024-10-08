import asyncio

from fastapi.testclient import TestClient

from app.api import dependencies
from app.db import models
from app.main import app
from app.service.position_service import PositionService
from tests.db import sessionmaker_test


def _test_position_service() -> PositionService:
    return PositionService(sessionmaker=sessionmaker_test)


app.dependency_overrides[dependencies.get_position_service] = _test_position_service

client = TestClient(app)

_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
_opening = "french defense"
_description = "rated game"
_eval = 0.5


def test_enumerate_positions():
    # populate some data
    asyncio.run(_populate_data())

    # call api
    response = client.get("/positions/v1/1")

    # assert response
    expected = """[{"fen":"rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1","eval":0.5}]"""
    assert response.status_code == 200
    assert response.content == expected.encode()


async def _populate_data():
    db_game = models.Game(description=_description, opening=_opening)
    db_position = models.Position(fen=_fen, eval=_eval, games=[db_game])
    async with sessionmaker_test() as session:
        session.add(db_position)
        await session.commit()
