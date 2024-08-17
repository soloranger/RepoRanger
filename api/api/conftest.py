import pytest

from api import create_app
from api.object import db as database


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db():
    return database