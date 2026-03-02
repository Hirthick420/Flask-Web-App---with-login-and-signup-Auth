#This file has all the url/ this file is blueprint of our project
from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/') 
def home():
    return render_template("home.html")