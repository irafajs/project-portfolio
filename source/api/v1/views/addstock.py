#!/usr/bin/python3
"""
SHEBANG to create a py script
"""


from source.models.storage.connectdb import Connecttodb
from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from source.models.medecine import Addmedecine
from source.models.user import Adduser
import json


add_stock = Blueprint('add_stock', __name__)


@add_stock.route('/addstock', methods=['GET', 'POST'])
def addstock():
    """add new stock to the database"""
    if request.method == 'POST':
        user_email = session.get('user_email')
        connector = Connecttodb()
        pharm_det = connector.get_user_by_email(user_email)
        pharm_id = pharm_det.id
        med_name = request.form.get('medecine_name')
        med_description = request.form.get('description')
        quantity = request.form.get('quantity')

        if not (med_name and med_description and quantity):
            flash('All fields are required', category='error')
            return render_template("addstock.html")
        new_stock_data = Addmedecine(
            med_name=med_name,
            med_description=med_description,
            quantity=quantity,
            pharmacy_id=pharm_id
        )
        connector.new(new_stock_data)
        flash('Stock added successfully!', category='success')
        return render_template("addstock.html")

    return render_template("addstock.html")
