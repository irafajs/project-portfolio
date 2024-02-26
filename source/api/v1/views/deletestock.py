#!/usr/bin/python3
"""
SHEBANG to create a py script
"""


from source.models.storage.connectdb import Connecttodb
from flask import Blueprint, render_template, request
from flask import flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from source.models.medecine import Addmedecine
from source.models.user import Adduser
from source.auth import auth
import json


delete_stock = Blueprint('delete_stock', __name__)


@delete_stock.route('/delete/<string:med_id>', methods=['DELETE'])
def deletestock(med_id):
    """delete the whole medecine record"""
    if med_id:
        connector_d = Connecttodb()
        med = connector_d.get_data_by_med_id(med_id)
        if med:
            connector_d.delete_row(med)
            connector_d.close()
            return jsonify(
                {'message': f'{med.med_name} deleted', 'med_name': med.med_name}), 200
        else:
            return jsonify({'error': 'Medicine not found'}), 404
    else:
        return jsonify({'error': 'No ID was fetched'}), 400
