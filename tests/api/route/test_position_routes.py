import asyncio
import pytest

from fastapi.testclient import TestClient

from app.api import dependencies
from app.db import models
from app.main import app
from app.service.position_service import PositionService
from tests.db import sessionmaker_test


_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

@pytest.fixture(scope="session")
def client():
    # construct test client
    # TODO doesn't work, can't connet to redis
    app.dependency_overrides[dependencies.get_position_service] = _test_position_service
    with TestClient(app) as client:
        # populate some data
        asyncio.run(_populate_data())
        yield client

def test_enumerate_positions_with_eval(client):
    # call api
    response = client.get("/positions/v1/1")

    # assert response
    expected = f"""[{{"fen":"{_fen}","eval":1.2}}]"""
    assert response.status_code == 200
    assert response.content == expected.encode()


def test_enumerate_positions_no_eval(client):
    # call api
    response = client.get("/positions/v1/1?eval=false")

    # assert response
    expected = f"""[{{"fen":"{_fen}","eval":null}}]"""
    assert response.status_code == 200
    assert response.content == expected.encode()


async def _populate_data():
    db_game = models.Game(description="rated game", opening= "french defense")
    db_position = models.Position(fen=_fen, games=[db_game])
    async with sessionmaker_test() as session:
        session.add(db_position)
        await session.commit()

def _test_position_service() -> PositionService:
    return PositionService(sessionmaker=sessionmaker_test)

