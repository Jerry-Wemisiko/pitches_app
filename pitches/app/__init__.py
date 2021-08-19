from flask import Flask
from flask_login import LoginManager
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager

def create_app(config_name):
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])



    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app