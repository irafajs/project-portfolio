from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

user_details = Blueprint('views', __name__)


@user_details.route('/user_details', methods=['GET', 'POST'])
def home():
    return render_template("userdetails.html", user=current_user)
