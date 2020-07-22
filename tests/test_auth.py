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

def register(client, username, password, passwordConfirm, email, firstname, lastname):
  payload =  {
    'username' : username, 
    'password' : password, 
    'passwordConfirm' : passwordConfirm,
    'email' : email,
    'firstname' : firstname,
    'lastname' : lastname
  }
  return client.post('/auth/register', data=dumps(payload), headers=headers)

def login(client, username, password):
  payload = {
    'username' : username,
    'password' : password
  }
  return client.post('/auth/login', data=dumps(payload), headers=headers)

def logout(client):
  return client.post('/auth/logout', headers=headers)

def test_login_cycle(client):
  # test registration
  r = register(client, "testlogin", "testpsw", "testpsw", "test@test.com", "test", "test")
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