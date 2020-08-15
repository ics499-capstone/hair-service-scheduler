from flask import Blueprint, request, json, jsonify
from flask_api import status

import json
import logging
console = logging.getLogger('console')


API_URL = '/api/data/'

bp = Blueprint('data', __name__, url_prefix=API_URL)

@bp.route('/product', methods=['GET'])
def product():
  from flaskr.models import db, Product, UserAccount, ShoppingCart
  
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