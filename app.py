#!/usr/bin/python3
"""
app to run our project
"""


import source
from flask import Flask
from flask_login import LoginManager
from source.auth import auth
from source.api.v1.views.homepage import views
from source.api.v1.views.userdetails import user_details
from source.api.v1.views.addstock import add_stock
from source.api.v1.views.deletestock import delete_stock

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
app.config['TEMPLATE_FOLDER'] = 'templates'

app.config['SECRET_KEY'] = 'project_medication1'

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(user_details, url_prefix='/')
app.register_blueprint(add_stock, url_prefix='/')
app.register_blueprint(delete_stock, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Adduser.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
