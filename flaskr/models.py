import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Enum, ForeignKey, types
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from decimal import Decimal as D

class SqliteNumeric(types.TypeDecorator):
  impl = types.String
  def load_dialect_impl(self, dialect):
    return dialect.type_descriptor(types.VARCHAR(100))
  def process_bind_param(self, value, dialect):
    return str(value)
  def process_result_value(self, value, dialect):
    return D(value)

# initialize here instead
db = SQLAlchemy()

# over-ride the default Numeric
# db.Numeric = SqliteNumeric

class UserAccountType(int, enum.Enum):
  customer = 0
  employee = 1
  admin = 2

  @classmethod
  def exists(self, value):
    return value in UserAccountType.__members__.values()

# -----------------------------------------------------------
# useraccount table
# -----------------------------------------------------------
class UserAccount(UserMixin, db.Model): # inherit is_authenticated, is_active, is_anonymous, get_id from UserMixin
  __tablename__ = "useraccount"
  # primary key
  id = db.Column(db.Integer, primary_key=True)
  # username to log in
  username = db.Column(db.String(64), index=True, unique=True)
  # email address for registering
  email = db.Column(db.String(120), index=True, unique=True)
  # sha256 hash of the password
  password_hash = db.Column(db.String(128))
  # account priviledge
  type = db.Column(Enum(UserAccountType), nullable=False, default=0)

  # contraints
  __table_args__ = (db.UniqueConstraint('username', 'email'),)

  # contructor
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password_hash = generate_password_hash(password, method='sha256')
    self.type = UserAccountType.customer
    # self.register_date = datetime.now()

  #def __repr__(self):
    #return '(UserAccoount) {}:{}:admin={}'.format(self.username, self.email, self.type)

  def authenticate(self, password):
    return check_password_hash(self.password_hash, password)

# -----------------------------------------------------------
# product table
# -----------------------------------------------------------
class Product(db.Model):
  __tablename__ = "product"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), nullable=True)
  description = db.Column(db.String(512), nullable=False)
  quantity = db.Column(db.Integer, nullable=False, default=0)
  price = db.Column(db.Numeric(5, 2), nullable=False)
  image = db.Column(db.String(256), nullable=True)

  # product constructor
  def __init__(self, name, description, quantity, price, image=None):
    self.name = name
    self.description = description
    self.quantity = quantity
    self.price = price

  #def __repr__(self):
    #return '(Product) {}:x{}:${}:desc={}'.format(self.name, self.quantity, self.price, self.description)

# -----------------------------------------------------------
# cart table
# -----------------------------------------------------------
class ShoppingCart(db.Model):
  __tablename__ = "cart"
  id = db.Column(db.Integer, primary_key=True)
  account_id = db.Column(db.Integer, db.ForeignKey('useraccount.id'), nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
  # amount to buy
  quantity = db.Column(db.Integer, default=0)

  # shopping cart constructor (it is actually a relationship with extra attributes)
  def __init__(self, account_id, product_id, quantity):
    self.account_id = account_id
    self.product_id = product_id
    self.quantity = quantity

# -----------------------------------------------------------
# service table
# -----------------------------------------------------------
class Service(db.Model):
  __tablename__ = "service"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), nullable=True)
  description = db.Column(db.String(512), nullable=True)
  price = db.Column(db.Numeric(5, 2), nullable=True)

  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price

# -----------------------------------------------------------
# Appointment (AKA Scheduler)
# -----------------------------------------------------------
class Appointment(db.Model):
  __tablename__ = "appointment"
  id = db.Column(db.Integer, primary_key=True)
  account_id = db.Column(db.Integer, db.ForeignKey('useraccount.id'), nullable=False)
  service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
  date = db.Column(db.DateTime)

  def __init__(self, account_id, service_id, date):
    self.account_id = account_id
    self.service_id = service_id
    self.date = date