import os

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

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
    JWT_SECRET_KEY='hide-this-for-dear-life',
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  CORS(app)

  import logging, logging.config, yaml

  # load the log configurations
  log_conf = yaml.safe_load(open('./logging.yaml'))
  # use the log configuration
  logging.config.dictConfig(log_conf)
  # init a log instance
  console = logging.getLogger('console')
  console.debug('Starting application')

  # register the SQLAlchemy instance with flask
  from flaskr.models import db
  db.init_app(app)

  # register the Login_Manager instance with flask
  from flaskr.auth import login_manager
  login_manager.init_app(app)

  # registers the custom commands with flask
  from . import commands
  commands.init_app(app)

  # registers the migrations with flask
  migrate = Migrate(app, db)

  # registers the api blueprints with flask
  from . import auth, admin
  app.register_blueprint(auth.bp)
  app.register_blueprint(admin.bp)

  from flaskr.jwt import jwt
  jwt.init_app(app)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  return app