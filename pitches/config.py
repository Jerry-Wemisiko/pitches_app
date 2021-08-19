import os
from re import DEBUG

from flask import config

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:skyles@localhost/pitches'

    #mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    SQLALCHEMY_I = os.environ.get("DATABASE_URL")  
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://moringa:skyles@localhost/pitches_test'
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:skyles@localhost/pitches'
    DEBUG = True

config_options= {
    'development': DevConfig,
    'prodection':ProdConfig,
    'test':TestConfig
}
