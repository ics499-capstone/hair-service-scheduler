from flask import Blueprint, request, json, jsonify
from flaskr.jwt import admin_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

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
    return '400 Bad Request - missing fields', 400

  from flaskr.models import db, Product

  name = request.get_json()['name']
  description = request.get_json()['description']
  quantity = request.get_json()['quantity']
  price = request.get_json()['price']

  product = Product.query.filter_by(name=name).first()
  if product:
    return '409 Product already exist', 409

  # create the product
  product = Product(name, description, quantity, price)
  db.session.add(product)
  db.session.commit()

  result = {
    "status": "success",
  }
  return jsonify({"results": result}), 201