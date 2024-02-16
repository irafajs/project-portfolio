from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

add_stock = Blueprint('add_stock', __name__)


@add_stock.route('/addstock', methods=['GET', 'POST'])
def addstock():
    return render_template("addstock.html", user=current_user)
