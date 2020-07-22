import os

from flask import Flask
from flask_migrate import Migrate

# app factory func
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)

  # configurations
  app.config.from_mapping(
    SECRET_KEY='dev',
    # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///app.db',
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # initialize to app but not yet bind
  from flaskr.models import db
  db.init_app(app) # must go after loading config

  from flaskr.auth import login_manager
  login_manager.init_app(app)

  # init migration
  migrate = Migrate(app, db)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # register blueprints
  from . import auth
  app.register_blueprint(auth.bp)

  return app