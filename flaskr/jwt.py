# jwt.py
from functools import wraps
from flask_jwt_extended import (
  JWTManager, 
  jwt_required, 
  verify_jwt_in_request,
  get_jwt_identity
)
from flask import jsonify
from flaskr.models import UserAccount, UserAccountType

# for http status code
from flask_api import status

jwt = JWTManager()

''' # ---------------------------------
  Description:
    Custom decorators for admin users

  Usage:
    @admin_required
''' # ---------------------------------
def admin_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    verify_jwt_in_request()
    user = get_jwt_identity()
    account = UserAccount.query.filter_by(username=user).first()
    if (account.type != UserAccountType.admin):
      result = {
        "status": "failure",
        "message": "Only admins are allowed!"
      }
      return jsonify({"results": result}), status.HTTP_403_FORBIDDEN
    else:
      return fn(*args, **kwargs)
  return wrapper

''' # ---------------------------------
  Description:
    Custom decorators for customers

  Usage:
    @client_required
''' # ---------------------------------
def client_required(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    verify_jwt_in_request()
    user = get_jwt_identity()
    account = UserAccount.query.filter_by(username=user).first()
    if (account.type != UserAccountType.customer):
      result = {
        "status": "failure",
        "message": "Only customer are allowed!"
      }
      return jsonify({"results": result}), status.HTTP_403_FORBIDDEN
    else:
      return fn(*args, **kwargs)
  return wrapper