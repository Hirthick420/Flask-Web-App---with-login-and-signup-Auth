#This file has the auth routes like login and signup
from flask import Blueprint 

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>Login successful <p>"

@auth.route('/logout')
def logout():
    return "<p>Logout succesful <p>"

@auth.route('/sign-up')
def signup():
    return "<p> This is the signup page"
