import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Enum, ForeignKey
from werkzeug.security import generate_password_hash
from datetime import datetime

# initialize here instead
db = SQLAlchemy()

class UserAccountType(enum.Enum):
  customer = 0
  employee = 1
  admin = 2

# useraccount table
class UserAccount(db.Model):
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
  # register_date = db.Column(db.DateTime, nullable=False)
  # register_confirmed = db.Column(db.Boolean, nullable=False, default=False)
  # register_complete = db.Column(db.DateTime, nullable=True, default=False)

  # contraints
  __table_args__ = (db.UniqueConstraint('username', 'email'),)

  # contructor
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password_hash = generate_password_hash(password, method='sha256')
    self.type = UserAccountType.customer
    self.register_date = datetime.now()

  def __repr__(self):
    return '<UserAccount {}>\n\t{}\n\t{}'.format(self.username, self.email, self.phone_number)

# user table
class User(db.Model):
  __tablename__ = "user"
  # primary key
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(64), nullable=False)
  lastname = db.Column(db.String(64), nullable=False)
  account_id = db.Column(db.Integer, db.ForeignKey('useraccount.id'), nullable=False)

  def __init__(self, firstname, lastname, account_id):
    self.firstname = firstname
    self.lastname = lastname
    self.account_id = account_id

