import pytest
from bs4 import BeautifulSoup


@pytest.mark.unit
def test_index_welcomes_nrao(client):
    """
    Verify that the web page includes the string 'Hello NRAO!'
    """
    response = client.get("/")
    soup = BeautifulSoup(response.text, "html.parser")
    welcome = soup.find("h2")
    assert "Hello NRAO!" in welcome.get_text()


@pytest.mark.unit
def test_nrao_text_links_to_nrao_edu(client):
    """
    Verify that the NRAO text links to hrao.edu
    """
    response = client.get("/")
    soup = BeautifulSoup(response.text, "html.parser")
    nrao_text = soup.find(string="NRAO")

    assert nrao_text is not None

    link = nrao_text.find_parent("a")
    assert link is not None
    assert "href" in link.attrs
    assert "public.nrao.edu" in link.attrs["href"]
