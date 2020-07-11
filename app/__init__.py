from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS

# instantiate the application, database and migration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATION')

db = SQLAlchemy(app) # using for ORM
migrate = Migrate(app, db)
CORS(app)

@app.route('/api/user/register', methods=['POST'])
def register():
  json = request.get_json()
  transaction_keys = ['username' , 'email', 'password', 'passwordConfirm']

  if not all (key in json for key in transaction_keys):
    return 'Something Missing' , 400

  email = request.get_json()['email']
  print(email)
  # return results
  result = {
    "email": "asd"
  }
  return jsonify({"results": result}), 201