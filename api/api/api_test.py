import pytest



def test_env(app):
    assert app.config.get("ENV") == "test"
    
def test_debug(app):
    assert app.config.get("DEBUG") is True
    
def test_database(app, db):
    with app.app_context():
        assert db.engine.url.database == "test"
        # REPORANGER_API_DATABASE_URL=mysql+pymysql://root:root@localhost:3306/test