from flask import Blueprint, request, json, jsonify
from flask_api import status

import json
import logging
console = logging.getLogger('console')


API_URL = '/api/data/'

bp = Blueprint('data', __name__, url_prefix=API_URL)

# this endpoint sends all product to the frontend
@bp.route('/product', methods=['GET'])
def product():
  from flaskr.models import db, Product
  
  query = Product.query
  data = query.all()

  arr = [] # array of dictionary
  for i in data:
    arr.append({
      'id' : i.id,
      'name' : i.name,
      'description' : i.description,
      'price' : float(i.price),
      'quantity' : i.quantity
    })

  return jsonify(product=arr), status.HTTP_200_OK

# this endpoint sends all the available services to the frontend
@bp.route('/service', methods=['GET'])
def service():
  from flaskr.models import db, Service
  
  query = Service.query
  data = query.all()

  arr = [] # array of dictionary
  for i in data:
    arr.append({
      'id' : i.id,
      'name' : i.name,
      'description' : i.description,
      'price' : float(i.price)
    })

  return jsonify(service=arr), status.HTTP_200_OK