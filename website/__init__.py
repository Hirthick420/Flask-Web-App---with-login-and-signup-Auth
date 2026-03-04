#This file will make website folder a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app(): #creating a function
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'hirthick123' #Never share this secret key for developing purpose
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    #This is the connection part of auth.py and views.py
    from .auth import auth #from the auth file import auth which is the blueprint
    from .views import views #from the views file import auth which is the blueprint

    '''
    what url_prefix / mean no prefix and can acces the page using just / no need to add anything 
    if anything is added add it to auth.py nd views.py as in route
    
    '''
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 

    from .models import User, Note
    create_database(app) #This a database creation function
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where should redirect if not logged in
    login_manager.init_app(app) #Telling the login manager which app we used

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')


