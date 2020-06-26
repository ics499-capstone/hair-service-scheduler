from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# instantiate the application, database and migration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATION')

db = SQLAlchemy(app) # using for ORM
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def home():
	return "<h1>Home Page</h1>"
