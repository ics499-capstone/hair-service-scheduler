import os
import tempfile
import pytest
import json
import ast

from flaskr import create_app
from json import dumps
from flask import request, json
from flask_api import status

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

API_URL = '/api/auth/'

@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True

  with app.test_client() as client:
    yield client

def register(client, username, password, email):
  payload =  {
    'username' : username, 
    'password' : password, 
    'email' : email
  }
  return client.post(''.join((API_URL, 'register')), data=dumps(payload), headers=headers)

def login(client, username, password):
  payload = {
    'username' : username,
    'password' : password
  }
  return client.post(''.join((API_URL, 'login')), data=dumps(payload), headers=headers)

def logout(client):
  return client.post(''.join((API_URL, 'logout')), headers=headers)

def test_login_cycle(client):
  # test registration
  r = register(client, "testlogin", "testpsw", "test@test.com")
  assert r.status_code == status.HTTP_409_CONFLICT

  # test logging in
  r = login(client, "testlogin", "testpsw")
  # r_dic = ast.literal_eval(r.data.decode("utf-8"))
  assert r.status_code == status.HTTP_201_CREATED

  # test logging out
  r = logout(client)
  assert r.status_code == status.HTTP_201_CREATED

  # test logging in with bad credentials
  r = login(client, "notauser", "notauser")
  assert r.status_code == status.HTTP_401_UNAUTHORIZED