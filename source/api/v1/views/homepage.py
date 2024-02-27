#!/usr/bin/python3
"""
SHEBANG to create a py script
"""


from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from source.models.storage.connectdb import Connecttodb
from source.models.medecine import Addmedecine
from source.models.user import Adduser

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    """define the home page and search function"""
    if request.method == 'POST':
        med_name = request.form.get('Search')
        connector = Connecttodb()
        medecine_info = connector.get_data_by_name(med_name)
        if medecine_info:
            pharmacy_data_list = []
            medecine_data_list = []
            for medecine in medecine_info:
                pharmacy_info = connector.get_data_by_id(medecine.pharmacy_id)
                medecine_data = {
                    'med_name': medecine.med_name,
                    'med_description': medecine.med_description
                }
                pharmacy_data = {
                    'pharmacy_name': pharmacy_info.pharmacy_name,
                    'address': pharmacy_info.address,
                    'phonenumber': pharmacy_info.phonenumber
                }
                medecine_data_list.append(medecine_data)
                pharmacy_data_list.append(pharmacy_data)
            return render_template("search.html", medecine=medecine_data_list, pharmacy=pharmacy_data_list)
        if not medecine_info:
            return render_template("nomed.html")
    elif request.method == 'GET':
        return render_template("home.html")
