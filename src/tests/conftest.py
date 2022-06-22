from fastapi.testclient import TestClient
from main import app
from src.database.db import get_host
import pytest


@pytest.fixture(scope="function")
def client(monkeypatch):
    monkeypatch.setenv(name="database_collection_name", value="test", prepend=False)

    with TestClient(app) as c:
        yield c

    db = get_host()
    db.drop_collection("users")

