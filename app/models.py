from app import db

class UserAccount(db.Model):
	# primary key
	id = db.Column(db.Integer, primary_key=True)
	# username to log in
	username = db.Column(db.String(64), index=True, unique=True)
	# email address for registering
	email = db.Column(db.String(120), index=True, unique=True)
	# sha256 hash of the password
	password_hash = db.Column(db.String(128))
	# phone number
	phone_number = db.Column(db.String(20), nullable=True)
	# the type of the account (role)

	def __repr__(self):
		return '<User {}>\n\t{}\n\t{}'.format(self.username, self.email, self.phone_number)