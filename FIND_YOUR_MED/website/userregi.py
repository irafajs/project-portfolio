#!/usr/bin/python3


from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask

app = Flask(__name__)

class User:
    env_file_path = "/home/jirafasha/Desktop/MED_FINDER/website"
    load_dotenv(dotenv_path=os.path.join(env_file_path, ".env"))
    dname = os.getenv("DATABASE_NAME")
    duser = os.getenv("DATABASE_USER")
    dhost = os.getenv("DATABASE_HOST")
    dpassword = os.getenv("DATABASE_PASSWORD")
    dport = os.getenv("DATABASE_PORT")

    db = create_engine(f'mysql+mysqldb://{duser}:{dpassword}@{dhost}:{dport}/{dname}')
    connection = db.connect()
    metadata = MetaData()
    inspector = inspect(db)
    existing_tables = inspector.get_table_names()

    if 'pharm_user' not in existing_tables:
        pharm_user = Table(
            'pharm_user',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('pharmacy_name', String(255)),
            Column('phonenumber', String(20)),
            Column('address', String(255)),
            Column('pharmacy_mail', String(255)),
	    bind=db
        )
        metadata.create_all(bind=db)

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        pharmacy_name = request.form.get('pharmacyName')
        phone_number = request.form.get('phonenumber')
        full_address = request.form.get('fulladdress')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Perform some basic form validation
        if not (email and pharmacy_name and phone_number and full_address and password1 and password2):
            return "All fields are required"
        if password1 != password2:
            return "Passwords do not match"

        # Add the new user to the database
        User.pharm_user.insert().values(pharmacy_name=pharmacy_name, phonenumber=phone_number, address=full_address, pharmacy_mail=email).execute()

        # Optionally, you may redirect the user to a different page after successful signup
        return redirect(url_for('auth.login'))  # Assuming you have a login route named 'auth.login'

    # Render the sign-up form template for GET requests
    return render_template('sign_up.html')  # Assuming you have a sign-up form template
