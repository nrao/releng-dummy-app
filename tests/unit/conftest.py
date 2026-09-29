
from flask import Flask
import pytest
# from reportportal_client import RPLogger

from dummy_app import init_app

# logger = RPLogger("pytest")


@pytest.fixture(scope="session")
def app():
    test_config = {
        "TESTING": True
    }
    app = init_app(test_config)

    with app.app_context():
        yield app

@pytest.fixture()
def client(app: Flask):
    return app.test_client()
