from flask import Blueprint, request, json, jsonify
from flaskr.jwt import admin_required
from flask_api import status

import logging
console = logging.getLogger('console')

API_URL = '/api/admin/'

bp = Blueprint('admin', __name__, url_prefix=API_URL)

''' # ---------------------------------
  Description:
    adds a product to the system
    note: this endpoint does not increase the quantity

  Endpoint:
    /admin/addproduct

  Parameters:
    name (string):
    description (string):
    quantity (int):
    price (float):

  Permission:
    admins

  Return:

''' # ---------------------------------
@bp.route('/addproduct', methods=['POST'])
@admin_required
def addproduct():
  json = request.get_json()
  transaction_keys = ['name', 'description', 'quantity', 'price']
  if (
      not all (key in json for key in transaction_keys) or
      not request.is_json
     ):
    return 'Missing fields', status.HTTP_400_BAD_REQUEST

  from flaskr.models import db, Product

  name = request.get_json()['name']
  description = request.get_json()['description']
  quantity = request.get_json()['quantity']
  price = request.get_json()['price']

  product = Product.query.filter_by(name=name).first()
  if product:
    return 'Product already exist', status.HTTP_409_CONFLICT

  # create the product
  product = Product(name, description, quantity, price)
  db.session.add(product)
  db.session.commit()

  console.debug('{} added!'.format(product))

  result = {
    "status": "success",
  }
  return jsonify({"results": result}), status.HTTP_201_CREATED