import os

import httpx
import pytest

@pytest.fixture()
def client():
    url = os.getenv("TEST_BASE_URL", "http://localhost:8000")
    with httpx.Client(base_url=url) as client:
        yield client
