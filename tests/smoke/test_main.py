import re

def test_root_is_accessible(client):
    response = client.get("/")

    assert response.status_code == 200
