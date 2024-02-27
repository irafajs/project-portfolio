#!/usr/bin/python3
"""
SHEBANG to create a py script
"""


from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
import json
from source.models.storage.connectdb import Connecttodb

user_details = Blueprint('user_details', __name__)


@user_details.route('/admin_profile', methods=['GET', 'POST', 'DELETE'])
def profile():
    delete_data = request.args.get('Delete')
    user_email = session.get('user_email')
    connector = Connecttodb()
    pharm_det = connector.get_user_by_email(user_email)
    pharm_id = pharm_det.id
    pharm_name = pharm_det.pharmacy_name
    u_s_det = connector.get_data_by_pharm_id(pharm_id)
    connector.close()
    if not u_s_det:
        return render_template("nodata.html", pharm_name=pharm_name)
    else:
        pharmacy_data_list = []
        for medecine in u_s_det:
            medecine_data = {
                'med_id': medecine.id,
                'med_name': medecine.med_name,
                'med_description': medecine.med_description,
                'quantity': medecine.quantity
                }
            pharmacy_data_list.append(medecine_data)
    return render_template("profile.html", medecines=pharmacy_data_list, pharm_name=pharm_name)
