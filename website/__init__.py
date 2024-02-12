from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .storage.connectdb import Adduser


def create_app():
    app = Flask(__name__)
    app.config['STATIC_FOLDER'] = 'static'
    app.config['SECRET_KEY'] = 'project_1'

    from .views.homepage import views
    from .views.userdetails import user_details 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
