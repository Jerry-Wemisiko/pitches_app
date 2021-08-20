import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:SKYLES@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    

    #mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  
    pass

class DevConfig(Config):
    DEBUG = True

config_options= {
    'development': DevConfig,
    'production':ProdConfig,
}
