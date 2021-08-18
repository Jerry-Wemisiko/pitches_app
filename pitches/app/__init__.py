from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask import Flask
from flask_mail import Mail
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


    # Creating the app configurations
    app.config.from_object(config_options[config_name])
   
    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app