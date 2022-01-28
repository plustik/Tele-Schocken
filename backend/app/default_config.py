
import os


class DefaultConfig(object):
    ENV = "production"

    SERVER_NAME = "example.com"
    APPLICATION_ROOT = "/"

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = 'Strict'

    MAX_CONTENT_LENGTH = 1024 * 1024 * 16
