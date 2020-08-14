import os
import tempfile
import pytest
import json
import ast

from flaskr import create_app
from json import dumps
from flask import request, json
from flask_api import status

AUTH_URL = '/api/auth/'
ADMIN_URL = '/api/admin/'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def auth_header(r):
  # extract the token
  token = r.get_json()['access_token']
  # add it to the header
  auth_header = ''.join(('Bearer ', token))
  # build new header
  headers = {
    'Content-type': 'application/json', 
    'Accept': 'text/plain',
    'Authorization': auth_header
  }
  return headers

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
  return client.post(''.join((AUTH_URL, 'register')), data=dumps(payload), headers=headers)

def login(client, username, password):
  payload = {
    'username' : username,
    'password' : password
  }
  return client.post(''.join((AUTH_URL, 'login')), data=dumps(payload), headers=headers)

def logout(client):
  return client.post(''.join((AUTH_URL, 'logout')), headers=headers)

def add_product(client, name, description, quantity, price, headers=headers):
  payload = {
    'name' : name,
    'description' : description,
    'quantity' : quantity,
    'price' : price
  }
  return client.post(''.join((ADMIN_URL, 'addproduct')), data=dumps(payload), headers=headers)

def del_product(client, name, headers=headers):
  payload = {
    'name' : name
  }
  return client.post(''.join((ADMIN_URL, 'delproduct')), data=dumps(payload), headers=headers)

def add_role(client, username, role, headers=headers):
  payload = {
    'username' : username,
    'role' : role
  }
  return client.post(''.join((ADMIN_URL, 'addrole')), data=dumps(payload), headers=headers)