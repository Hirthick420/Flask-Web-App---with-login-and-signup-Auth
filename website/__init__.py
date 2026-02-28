#This file will make website folder a python package
from flask import Flask

def create_app(): #creating a function
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'hirthick123' #Never share this secret key for developing purpose

    #This is the connection part of auth.py and views.py
    from .auth import auth #from the auth file import auth which is the blueprint
    from .views import views #from the views file import auth which is the blueprint

    '''
    what url_prefix / mean no prefix and can acces the page using just / no need to add anything 
    if anything is added add it to auth.py nd views.py as in route
    
    '''
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 
    return app


