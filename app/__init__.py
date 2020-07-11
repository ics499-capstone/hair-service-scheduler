from flask import Flask, Blueprint, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS

from .models import db
from .register import register_bp

# instantiate the application, database and migration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

migrate = Migrate(app, db)
CORS(app)

db.init_app(app)

# register the endpoint for registration
app.register_blueprint(register_bp)