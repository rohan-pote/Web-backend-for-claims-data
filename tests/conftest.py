from collections.abc import Iterable

import pytest
from fastapi.testclient import TestClient

from src.claim_service.app import app


@pytest.fixture
def client() -> Iterable[TestClient]:
    with TestClient(app) as client:
        yield client

