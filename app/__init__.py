from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_cors import CORS
from .models import UserAccount


# instantiate the application, database and migration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATION')

db = SQLAlchemy(app) # using for ORM
migrate = Migrate(app, db)
CORS(app)

@app.route('/api/user/register', methods=['POST'])
def register():
  try:
    json = request.get_json()
    transaction_keys = ['username' , 'email', 'password', 'passwordConfirm']

    if not all (key in json for key in transaction_keys):
      return '400 Bad Request - missing fields', 400

    username = request.get_json()['username']
    email = request.get_json()['email']
    password = request.get_json()['password']
    passwordConfirm = request.get_json()['passwordConfirm']

    # check if there is already a user logged in
    # check if useraccount already exist
    useraccount_username = UserAccount.query.filter_by(username=username).first()
    if  useraccount_username:
      return '409 User already exist', 409

    # check if email already exist
    useraccount_email = UserAccount.query.filter_by(email=email).first()
    if useraccount_email:
      return '409 Existing account with associated email', 409

    # check if the password is equal to passwordConfirm
    if password != passwordConfirm:
      return '401 Password mismatch', 401

    # create the useraccount
    newaccount = UserAccount(username, email, password)

    # add the user to database
    db.session.add(newaccount)
    db.session.commit()

    # return some info back to client
    # return results
    result = {
      "status": "asd"
    }
    return jsonify({"results": result}), 201
  except:
    return '503 Service Unavailable', 503