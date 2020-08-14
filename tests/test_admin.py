from flask import request, json
from flask_api import status

from func import client, add_product, del_product, login, logout, auth_header

# test: regular user trying to enlist a product for sale
def test_user_addproduct(client):
  # name, description, quantity, price
  r = add_product(client, "shampoo", "kiwi scent shampoo", 5, 9.99)
  # requires admin permission
  assert r.status_code == status.HTTP_401_UNAUTHORIZED

# test: admin user adding a product to the system
def test_admin_addproduct(client):
  # log out if need be
  logout(client)
  # log in admin account
  r = login(client, 'admintest', 'admintest')
  # extract the token and build new header with admin jwt
  headers = auth_header(r)
  # now add the product
  r = add_product(client, "shampoo", "kiwi scent shampoo", 5, 9.99, headers)
  # product created successfully or already exist
  assert r.status_code == status.HTTP_201_CREATED or r.status_code == status.HTTP_409_CONFLICT

# test: regular user trying to delete product from the database
def test_user_delproduct(client):
  r = del_product(client, "shampoo")
  # requires admin permission
  assert r.status_code == status.HTTP_401_UNAUTHORIZED

# test: admin user trying to delete product from the database
def test_admin_delproduct(client):
  # log out if need be
  logout(client)
  # log in admin account
  r = login(client, 'admintest', 'admintest')
  # extract the token and build new header with admin jwt
  headers = auth_header(r)
  # add a product
  add_product(client, "shampoo", "kiwi scent shampoo", 5, 9.99, headers)
  # delete the product
  r = del_product(client, "shampoo", headers)
  # should be able to
  assert r.status_code == status.HTTP_200_OK