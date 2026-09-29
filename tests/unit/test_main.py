
import pytest


@pytest.mark.unit
def test_index_welcomes_nrao(client):
    """
    Verify that the web page includes the string 'Hello NRAO!'
    """
    response = client.get("/")
    assert b"Hello NRAO!" in response.data
