from flask import Blueprint, request, json, jsonify
from flaskr.jwt import client_required
from flask_api import status
# from flask_jwt import get_jwt_identity
from flask_jwt_extended import get_jwt_identity

API_URL = '/api/product/'

bp = Blueprint('product', __name__, url_prefix=API_URL)

''' # ---------------------------------
  Description:
    adds a product to the user's account
    note: this endpoint does not increase the quantity

  Endpoint:
    api/product/addcart

  Permission:
    customer

  Return:

''' # ---------------------------------
@bp.route('/addcart', methods=['POST'])
@client_required
def addcart():
  json = request.get_json()
  transaction_keys = ['product_id', 'quantity']
  if (
      not all (key in json for key in transaction_keys) or
      not request.is_json
     ):
    return 'Missing fields', status.HTTP_400_BAD_REQUEST

  from flaskr.models import db, Product, UserAccount, ShoppingCart

  product_id = request.get_json()['product_id']
  quantity = request.get_json()['quantity']

  # first check if the product even exists in the database
  product = Product.query.filter_by(id=product_id).first()
  if product is None:
    return 'Product does not exist', status.HTTP_400_BAD_REQUEST

  # check if the quantity exceeds what is available
  print('Amount user want: {}'.format(quantity))
  print('Amount in stock: {}'.format(product.quantity))
  if quantity > product.quantity:
    return 'Insufficient quantity added to cart', status.HTTP_400_BAD_REQUEST

  # get the user's account id (identity bounded to username)
  user = UserAccount.query.filter_by(username=get_jwt_identity()).first()
  # print(user.username)

  # try to find if user already have the item in the cart
  product_cart = ShoppingCart.query \
                 .filter_by(product_id=product_id) \
                 .filter_by(account_id=user.id) \
                 .first()

  # add the product to users cart
  if product_cart is None:
    product_cart = ShoppingCart(user.id, product_id, quantity)
  else:
    print('Amount user already have: {}'.format(product_cart.quantity))
    # if the quantity wanted + the quantity inside cart exceeds the quantity available
    if (product_cart.quantity + quantity) > product.quantity:
      # assign all quantity available to the user's cart
      product_cart.quantity = product.quantity
    else:
      # otherwise just add the remaining
      product_cart.quantity = product_cart.quantity + quantity
  
  print('Total amount user now have in cart: {}'.format(product_cart.quantity))
  
  db.session.add(product_cart)
  db.session.flush()
  db.session.commit()

  return jsonify({
    "status": "success",
    "quantity": product_cart.quantity # return the amount in cart back
  }), status.HTTP_202_ACCEPTED


  
