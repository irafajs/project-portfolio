from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

user_details = Blueprint('user_details', __name__)


@user_details.route('/admin_profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html", user=current_user)
