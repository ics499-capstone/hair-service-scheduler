from flask import Blueprint, request, json, jsonify
from flaskr.jwt import client_required
from flask_api import status
from flask_jwt_extended import get_jwt_identity

from flaskr.models import db, Service, Appointment, UserAccount

import json
import logging
console = logging.getLogger('console')

API_URL = '/api/service/'

bp = Blueprint('service', __name__, url_prefix=API_URL)

''' # ---------------------------------
  Description:
    schedules a service

  Endpoint:
    api/service/schedule

  Permission:
    customer

  Return:

''' # ---------------------------------
@bp.route('/schedule', methods=['POST'])
@client_required
def addcart():
  json = request.get_json()
  transaction_keys = ['service_id', 'time']
  if (not all (key in json for key in transaction_keys) or not request.is_json):
    return 'Missing fields', status.HTTP_400_BAD_REQUEST

  service_id = request.get_json()['service_id']
  time = request.get_json()['time']

  # first check if the service even exists in the database
  service = Service.query.filter_by(id=service_id).first()
  if service is None:
    return 'Service does not exist', status.HTTP_400_BAD_REQUEST

  # get the user's account id (identity bounded to username)
  user = UserAccount.query.filter_by(username=get_jwt_identity()).first()

  # try to find if user already have the service in their schedule
  service_cart = Appointment.query \
                 .filter_by(service_id=service_id) \
                 .filter_by(account_id=user.id) \
                 .first()

  # if it isnt in the service cart, schedule the apointment
  if service_cart is None:
    service_cart = Appointment(user.id, service_id, time)
  else:
    # otherwise no further actions needed
    return 'Service is already scheduled', status.HTTP_400_BAD_REQUEST

  db.session.add(service_cart)
  db.session.flush()
  db.session.commit()

  return jsonify({
    "status": "success"
  }), status.HTTP_202_ACCEPTED

''' # ---------------------------------
  Description:
    return the users cart

  Endpoint:
    api/service/getcart

  Permission:
    customer

  Return:

''' # ---------------------------------
@bp.route('/getcart', methods=['POST'])
@client_required
def getcart():
  # get the user's account id (identity bounded to username)
  user = UserAccount.query.filter_by(username=get_jwt_identity()).first()

  # get all services in users schedule/appointment list
  query = (db.session.query(Appointment, Service) \
          .join(Service, Appointment.service_id == Service.id) \
          .add_columns( \
              Appointment.date, \
              Service.name, \
              Service.description, \
              Service.price) \
          .filter(Appointment.account_id == user.id))
  data = query.all()

  arr = [] # array of dictionary
  for i in data:
    arr.append({
      'quantity' : i[0].date,
      'name' : i[1].name,
      'description' : i[1].description,
      'price' : float(i[1].price)
    })

  return jsonify(cart=arr), status.HTTP_200_OK