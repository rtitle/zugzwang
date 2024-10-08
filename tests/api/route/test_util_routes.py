from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_path():
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["Location"] == "/docs"


def test_health_check():
    response = client.get("/health-check/")
    assert response.status_code == 200
