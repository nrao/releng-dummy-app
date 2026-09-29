
import re

from flask import json
import pytest

@pytest.mark.unit
def test_heathz_returns_version(client):
    response = client.get("/healthz")
    data = json.loads(response.data)
    assert "version" in data.keys(), '"version" should be present in the response'
    version = data["version"]
    assert re.match(r"\d+\.\d+\.\d+", version), f"{version} is not in the expected format x.y.z"
