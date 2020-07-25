import os
import tempfile
import pytest

from flaskr import create_app
from json import dumps
from flask import request, json

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
  assert b'409' in r.data # user already exist

  # test logging in
  r = login(client, "testlogin", "testpsw")
  assert r.json['results']['status'] == "success"

  # test logging out
  r = logout(client)
  assert r.json['results']['status'] == "success"

  # test logging in with bad credentials
  r = login(client, "notauser", "notauser")
  assert b'Invalid Username or Password' in r.data