import os
import tempfile
import pytest

from flaskr import create_app
from json import dumps
from flask import request, json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True

  with app.test_client() as client:
    yield client

