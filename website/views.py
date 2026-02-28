#This file has all the url/ this file is blueprint of our project
from flask import Blueprint 

views = Blueprint('views',__name__)

@views.route('/') 
def home():
    return "<h1> Hello there!! <h1>"