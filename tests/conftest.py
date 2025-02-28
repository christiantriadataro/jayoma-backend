# tests/conftest.py
import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from main import app
from fake_db import get_fake_db

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def fake_db():
    return get_fake_db()
