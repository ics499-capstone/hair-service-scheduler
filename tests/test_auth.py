from flask import request, json
from flask_api import status

from func import client, register, login, logout

def test_register(client):
  r = register(client, "testlogin", "testpsw", "test@test.com")
  assert r.status_code == status.HTTP_409_CONFLICT

def test_login(client):
  r = login(client, "testlogin", "testpsw")
  # r_dic = ast.literal_eval(r.data.decode("utf-8"))
  assert r.status_code == status.HTTP_201_CREATED

def test_logout(client):
  r = logout(client)
  assert r.status_code == status.HTTP_401_UNAUTHORIZED

def test_fake_login(client):
  r = login(client, "notauser", "notauser")
  assert r.status_code == status.HTTP_401_UNAUTHORIZED