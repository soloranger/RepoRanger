import pytest

from api import create_app
from api.object import db as database
from api.object import mg as migration

class TestStorage:
    def set(self, name, value):
        setattr(self, name, value)
        return True
    def get(self,  name):
        return getattr(self, name)
    
test_storage = TestStorage()

@pytest.fixture
def storage():
    return test_storage
    
@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db():
    return database


@pytest.fixture
def mg():
    return migration
