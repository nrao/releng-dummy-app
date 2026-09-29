
import pytest


@pytest.mark.unit
def test_index_welcomes_nrao(client):
    response = client.get("/")
    assert b"Hello NRAO!" in response.data
