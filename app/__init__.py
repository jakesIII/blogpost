from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
# instances
mail=Mail()
bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
# app function
def create_app(config_name):
    # instantiate flask
    app=Flask(__name__)
    # application configuration
    app.config.from_object(config_options[config_name])
    # extension initializing
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # blueprint reg.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # authentcation reg.
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authentcate')

    return app
