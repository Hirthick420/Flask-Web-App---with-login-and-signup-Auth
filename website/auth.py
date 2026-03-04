#This file has the auth routes like login and signup
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

from flask_login import login_required, login_user, logout_user, current_user
#we access current state of website with current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # checking if db email = from form email
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
                login_user(user, remember= True) #Login in the user and remembers the state
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email doesn\'t exists', category='error')


    return render_template("login.html", user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:    
            flash('Email already exists', category='error')
        elif len(email)<4:
            flash('Email too short must be greater than 4 char', category = 'error')
            pass
        elif len(first_name) < 2:
            flash('Firstname too short must be greater than 2 char', category = 'error')
        elif len(password1) < 7:
            flash('Password too short must be greater than 7', category = 'error')
            pass
        elif password1 != password2:
            flash('Password dont match', category = 'error')
            pass
        else:
            new_user = User(email=email,first_name=first_name,password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account created', category = 'success')
            return redirect(url_for('views.home')) #redirects to home page
            #add user to database

    return render_template("sign_up.html",user = current_user)

