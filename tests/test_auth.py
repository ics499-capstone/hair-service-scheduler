import pytest

def register(client, username, password, passwordConfirm, email, firstname, lastname):
  return client.post('/auth/register', data=dict(
    username=username,
    password=password,
    passwordConfirm=passwordConfirm,
    email=email,
    firstname=firstname,
    lastname=lastname
  ), follow_redirects=True)

def login(client, username, password):
  return client.post('/auth/login', data=dict(
    username=username,
    password=password
  ), follow_redirects=True)

def logout(client):
    return client.get('/auth/logout', follow_redirects=True)

def test_login_cycle(client):
  rv = register(client, "testlogin", "testpsw", "testpsw", "test@test.com", "test", "test")
  assert b'You are already a user' in rv.data

  rv = login(client, "testlogin", "testpsw")
  assert b'You were logged in' in rv.data

  rv = logout(client)
  assert b'You were logged out' in rv.data

  rv = login(client, "notauser", "notauser")
  assert b'Invalid username' in rv.data