from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import request, redirect, url_for
from source.models.user import Adduser
from source.models.storage.connectdb import Connecttodb


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        connector = Connecttodb()
        user = connector.get_user_by_email(email)
        print(user.pharmacy_mail)
        if user:
#            if check_password_hash(user.password, password):
            if user.password == password:
                flash('Logged in successfully!', category='success')
#                login_user(user, remember=True)
                return redirect(url_for('user_details.profile'))
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
        new_user = Adduser(
                pharmacy_name= pharmacy_name,
                phonenumber= phone_number,
                address= full_address,
                pharmacy_mail= email,
                password= password2
                )
        connector = Connecttodb()
        connector.new(new_user)
        return redirect(url_for('auth.login'))

    return render_template('sign_up.html')

