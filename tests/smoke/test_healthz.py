import re

def test_heathz_returns_version(client):
    response = client.get("/healthz")

    assert response.status_code == 200

    data = response.json()
    assert "version" in data.keys(), '"version" should be present in the response'
    version = data["version"]
    assert re.match(r"\d+\.\d+\.\d+", version), f"{version} is not in the expected format x.y.z"
