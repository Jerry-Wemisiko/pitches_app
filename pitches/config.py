import os

class Config:

     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jerry@localhost/pitches'

class ProdConfig:
      
      pass

class DevConfig:  
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jerry@localhost/pitches'
   
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}