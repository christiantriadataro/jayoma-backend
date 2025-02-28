import pytest
from fastapi.testclient import TestClient

from app.fake_db import FakeDB
from app.main import app

client = TestClient(app)

@pytest.fixture()
def fake_db():
    return FakeDB()

def test_get_categories_endpoint(client):
    response = client.get("/categories")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_get_category_endpoint(client):
    response = client.get("/categories/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1