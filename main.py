#THis is the file we run when we want to start our web server
from website import create_app

app = create_app()

'''
This is the main line why we have written main is if we import the createapp the 
server will run so we want the server to run only when we run the main.py
'''
if __name__ == '__main__': 
    app.run(debug =True)
