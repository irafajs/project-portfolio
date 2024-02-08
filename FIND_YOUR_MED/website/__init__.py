from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from website.storage.connectdb import Connectsqldb


def create_app():
    app = Flask(__name__)
    app.config['STATIC_FOLDER'] = 'static'
    app.config['SECRET_KEY'] = 'project_1'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format('pharmacy', 'Password_12345', '127.0.0.1', '3306', 'pharmacy_storage_db')
    db = SQLAlchemy(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
#    with app.app_context():
#       Connectsqldb.db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
