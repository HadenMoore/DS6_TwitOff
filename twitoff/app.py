# My Application
from flask import Flask

from .models import DB

#Make our own App Factory
def create_app():
    #Create Server
    app = Flask(__name__)

    #Add Config here later:
    app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #Add in DataBase init later
    DB.init_app(app)

    #Create the Route
    @app.route('/')

    #Define the Function
    def root():
        return 'Welcome to TwitOff!'

    return app
