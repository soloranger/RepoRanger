from os import environ


class Config:
    ENV = environ.get("REPORANGER_API_ENV", "production")

    DEBUG = bool(int(environ.get("REPORANGER_API_DEBUG", "0")))

    TESTING = bool(int(environ.get("REPORANGER_API_TESTING", "0")))

    SECRET_KEY = environ.get("REPORANGER_API_SECRET_KEY", "secretkey")

    SQLALCHEMY_DATABASE_URI = environ.get("REPORANGER_API_DATABASE_URL", None)

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
