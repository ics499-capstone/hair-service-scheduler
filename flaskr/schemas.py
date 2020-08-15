import warnings

with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  from flask_marshmallow import Marshmallow

from marshmallow_sqlalchemy import ModelSchema, fields
from flaskr.models import UserAccount, Product, ShoppingCart

ma = Marshmallow()

class SchemaUserAccount(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = UserAccount

class SchemaProduct(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Product

class SchemaShoppingCart(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = ShoppingCart
