import functools

from flask import Blueprint, flash, g, redirect, jsonify, request, json, session, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from json import dumps

# init login manager
login_manager = LoginManager()

bp = Blueprint('auth', __name__, url_prefix='/auth')

# user_loader callback to reload user object from user id stored in session
@login_manager.user_loader
def load_user(id):
  from flaskr.models import UserAccount
  return UserAccount.query.get(int(id))

''' # ---------------------------------
  Description:
    registers an account

  Endpoint:
    /auth/register

  Parameters:
    username (string):
    password (string):
    passwordConfirm (string):
    email (string):
    firstname (string):
    lastname (string):

  Return:
    string,int

''' # ---------------------------------
@bp.route('/register', methods=['POST'])
def register():
  json = request.get_json()
  transaction_keys = ['username' , 'email', 'password', 'passwordConfirm', 'firstname', 'lastname']
  if (
      not all (key in json for key in transaction_keys) or
      not request.is_json
     ):
    return '400 Bad Request - missing fields', 400

  # get DB context from models
  from flaskr.models import db, UserAccount, User

  username = request.get_json()['username']
  email = request.get_json()['email']
  password = request.get_json()['password']
  passwordConfirm = request.get_json()['passwordConfirm']
  firstname = request.get_json()['firstname']
  lastname = request.get_json()['lastname']

  # check if there is already a user logged in
  # check if useraccount already exist
  useraccount_username = UserAccount.query.filter_by(username=username).first()
  if useraccount_username:
    return '409 User already exist', 409

  # check if email already exist
  useraccount_email = UserAccount.query.filter_by(email=email).first()
  if useraccount_email:
    return '409 Existing account with associated email', 409

  # check if the password is equal to passwordConfirm
  if password != passwordConfirm:
    return '401 Password mismatch', 401

  # check if field exceed character length
  # check if email is in right format
  # check if password contains 1 uppercase, 1 special character, 1 number
    # re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')

  # create the useraccount
  newaccount = UserAccount(username, email, password)
  db.session.add(newaccount)
  db.session.flush() # update the id to constraint with user

  newuser = User(firstname, lastname, newaccount.id)
  db.session.add(newuser)

  # save
  db.session.commit()

  # tell the user to complete registration through email
  result = {
    "status": "success",
    "username": username,
    "email": email,
    "firstname": firstname,
    "lastname": lastname
  }
  return jsonify({"results": result}), 201

''' # ---------------------------------
  Description:
    logs into an existing account

  Endpoint:
    /auth/login

  Parameters:
    username (string):
    password (string):

  Return:
    string []: {firstname, lastname}

''' # ---------------------------------
@bp.route('/login', methods=['POST'])
def login():
  json = request.get_json()

  # check if needed fields are provided
  transaction_keys = ['username' , 'password']
  if (
      not all (key in json for key in transaction_keys) or
      not request.is_json
     ):
    return '400 Bad Request - missing fields', 400

  # check if user is already logged in
  if current_user.is_authenticated:
    return '409 User already logged in', 409

  username = request.get_json()['username']
  password = request.get_json()['password']

  from flaskr.models import db, UserAccount, User

  account = UserAccount.query.filter_by(username=username).first()
  if account is None or not account.authenticate(password):
    flash('Invalid Username or Password')
    return 'Invalid Username or Password', 401

  login_user(account)

  ''' # join data to return back to client
  userinfo = UserAccount.query\
             .join(User, UserAccount.id == User.id)\
             .add_columns(User.firstname, User.lastname)
             .filter(User.account_id == account.id)
  '''
  user = User.query.filter_by(account_id=account.id).first()
  account_type = dumps(account.type)
  result = {
    "status": "success",
    "firstname": user.firstname,
    "lastname": user.lastname,
    "username": account.username,
    "type": account_type
  }

  # create JSON web token
  access_token = create_access_token(identity=username)

  return jsonify({
    "results": result,
    "access_token": access_token
  }), 201

''' # ---------------------------------
  Description:
    log out an existing account

  Endpoint:
    /auth/logout

  Parameters:

  Return:
    string []: {firstname, lastname}

''' # ---------------------------------
@bp.route('/logout', methods=['POST'])
@login_required
def logout():
  logout_user()
  result = {
    "status": "success"
  }
  return jsonify({"results": result}), 201

''' # ---------------------------------
  Description:
    Protected view using jwt_required (requires a valid access token)

  Endpoint:
    /auth/test

  Parameters:

  Return:
    { "logged_in_as": user }

  Test:
    1) Log in (Hit endpoint: /auth/login)
    2) grab the "access_token" from the response
    3) Test
      3.1) Click Authorization Tab
      3.2) TYPE dropdown - Select: Bearer Token
      3.3) PASTE access_token copied from part 2 and paste into Token (right panel)
      3.4) Change the endpoint to /auth/test

''' # ---------------------------------
@bp.route('/test', methods=['POST'])
@jwt_required
def test():
    # Access the identity of the current user with get_jwt_identity
    user = get_jwt_identity()
    return jsonify(logged_in_as=user), 200

''' # ---------------------------------
  Description:
    Protected view using admin_required (requires a valid access token and admin rights)

  Endpoint:
    /auth/testadmin

''' # ---------------------------------
from flaskr.jwt import admin_required

@bp.route('/testadmin', methods=['POST'])
@admin_required
def testadmin():
    user = get_jwt_identity()
    return jsonify(logged_in_as=user), 200