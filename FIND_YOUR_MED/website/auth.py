from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import request, redirect, url_for
from .models import User
from .storage.connectdb import Connectsqldb
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    from flask import request, redirect, url_for,session
    from .models import User  # Assuming you have a User model defined
    from .storage.connectdb import Connectsqldb
    from sqlalchemy.orm import scoped_session, sessionmaker
    from sqlalchemy import create_engine
    from sqlalchemy import MetaData, Table, Column, Integer, String, inspect
    from dotenv import load_dotenv
    import os

    db_connector = Connectsqldb()
    
    if request.method == 'POST':
        email = request.form.get('email')
        pharmacy_name = request.form.get('pharmacyName')
        phone_number = request.form.get('phonenumber')
        full_address = request.form.get('fulladdress')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not (email and pharmacy_name and phone_number and full_address and password1 and password2):
            return "All fields are required"
        if password1 != password2:
            return "Passwords do not match"
        data = {
                'pharmacy_name': pharmacy_name,
                'phonenumber': phone_number,
                'address': full_address,
                'pharmacy_mail': email,
                'password': password2
                }
        env_file_path = "/home/jirafasha/Desktop/MED_FINDER/website"
        load_dotenv(dotenv_path=os.path.join(env_file_path, ".env"))
        dname = os.getenv("DATABASE_NAME")  # Replace "PATH_VARIABLE_NAME" with the actual variable name
        duser=os.getenv("DATABASE_USER") 
        dhost=os.getenv("DATABASE_HOST") 
        dpassword=os.getenv("DATABASE_PASSWORD") 
        dport=os.getenv("DATABASE_PORT")

        db = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(duser, dpassword, dhost,dport, dname))
        connection = db.connect()
        print("conntected to the db")
        db.session.add(data)
        db.session.commit()

        #Connectsqldb.new(data)
        #db_connector.new(data)
        # Optionally, you may redirect the user to a different page after successful signup
        return redirect(url_for('auth.login'))  # Assuming you have a login route named 'auth.login'

    # Render the sign-up form template for GET requests
    return render_template('sign_up.html')  # Assuming you have a sign-up form template

