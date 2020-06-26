import enum
from app import db
from sqlalchemy import Integer, Enum

class UserAccountType(enum.Enum):
	customer = 0
	employee = 1
	admin = 2

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
	# register date
	register_date = db.Column(db.DateTime, nullable=False)
	# register confirmation
	register_confirmed = db.Column(db.Boolean, nullable=False, default=False)
	# register confirmation date
	register_complete = db.Column(db.DateTime, nullable=True)

	def __repr__(self):
		return '<UserAccount {}>\n\t{}\n\t{}'.format(self.username, self.email, self.phone_number)