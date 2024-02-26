#!/usr/bin/python3
"""
SHEBANG TO make py script
"""


from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, session
from flask_login import login_required
from source.models.user import Adduser
from source.models.storage.connectdb import Connecttodb
import hashlib


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """method to allow an existing admin user to logon"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not (email and password):
            flash('All field must be filled to login.', category='error')
            return render_template("login.html")
        connector = Connecttodb()
        user = connector.get_user_by_email(email)
        if user:
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if user.password == hashed_password:
                session['user_email'] = email
                return redirect(url_for('user_details.profile'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    """method to logout user"""
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """method to allow pharmacy user to register"""
    if request.method == 'POST':
        email = request.form.get('email')
        pharmacy_name = request.form.get('pharmacyName')
        phone_number = request.form.get('phonenumber')
        full_address = request.form.get('fulladdress')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if not (email and pharmacy_name and phone_number and full_address and password1 and password2):
            flash('All fiels are required.', category='error')
            return render_template('sign_up.html')
        connector = Connecttodb()
        user = connector.get_user_by_email(email)
        if user:
            flash('Email already exists.', category='error')
        elif password1 != password2:
            flash('Password does not match.', category='error')
        else:
            new_user = Adduser(
                    pharmacy_name=pharmacy_name,
                    phonenumber=phone_number,
                    address=full_address,
                    pharmacy_mail=email,
                    password=hashlib.md5(password2.encode()).hexdigest()
                    )
            connector.new(new_user)
            flash('Account created successful.', category='SUCCESS')
            return redirect(url_for('auth.login'))

    return render_template('sign_up.html')
