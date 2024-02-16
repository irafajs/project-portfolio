#!/usr/bin/python3

from flask import Blueprint, render_template, request
#from source.models.storage.connectdb import Connecttodb
#from source.models.medecine import Addmedecine
#from source.models.user import Adduser 

def check_keyword():
    med_name = request.form.get("Search")
    print("Search keyword:", med_name)
    return "Check complete"
