from flask import Blueprint
from flask_restplus import Api, Resource, apidoc, fields

API_TITLE = 'Hair Service REST API'
API_DESCRIPTION = 'Hair Service REST API documentation and usage'

api = Api()
bp = Blueprint('api', __name__, url_prefix='/api')

def init_app(app):
  api.init_app(app, \
    version='1.0', \
    title=API_TITLE, \
    description=API_DESCRIPTION, \
  )

@bp.route('/doc/', endpoint='doc')
def swagger_ui():
  return apidoc.ui_for(api)
