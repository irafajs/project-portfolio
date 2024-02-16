#!/usr/bin/python3
from flask import Blueprint, render_template, request
from source.models.storage.connectdb import Connecttodb
from source.models.medecine import Addmedecine
from source.models.user import Adduser 

search = Blueprint('search', __name__)

@search.route('/search', methods=['GET', 'POST'])
def search_medecine():
    if request.method == 'POST':
        med_name = request.form.get('Search')
    else:
        med_name = request.args.get('Search')
    print(med_name)
    connector = Connecttodb()
    medecine_info = connector.get_data_by_name(med_name)
    if medecine_info:
        pharmacy_info = connector.get_user_by_id(medecine_info.pharmacie_id)
        medecine_data = {
            'med_name': medecine_info.med_name,
            'med_description': medecine_info.med_description
        }
        pharmacy_data = {
            'pharmacy_name': pharmacy_info.pharmacy_name,
            'address': pharmacy_info.address,
            'phonenumber': pharmacy_info.phonenumber
        }
        return render_template("search.html", medecine=medecine_data, pharmacy=pharmacy_data)
    else:
        return render_template("search.html", medecine=None, pharmacy=None)
    return render_template("search.html", medecine=None, pharmacy=None)
