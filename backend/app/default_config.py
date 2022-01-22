
import os


class DefaultConfig(object):
    #ENV = "production"
    ENV = "development"
    DEGUG = True

    SERVER_NAME = "127.0.0.1:5000"
    APPLICATION_ROOT = "/"

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'emailuser@example.com'
    MAIL_PASSWORD = 'emailpwd'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    #SESSION_COOKIE_NAME = None
    SESSION_COOKIE_DOMAIN = "example.com"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = 'Strict'

    MAX_CONTENT_LENGTH = 1024 * 1024 * 16
