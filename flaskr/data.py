from flask import Blueprint, request, json, jsonify
from flask_api import status

import json
import logging
console = logging.getLogger('console')


API_URL = '/api/data/'

#bp = Blueprint('data', __name__, url_prefix=API_URL)

#@bp.route('/register', methods=['POST'])