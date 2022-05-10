from flask import Flask
from config import config_options
from .main import views
from .extensions import db,bcrypt,login_manager,mail


def create_app(config_name):
    app = Flask(__name__)

    #Initializing flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app