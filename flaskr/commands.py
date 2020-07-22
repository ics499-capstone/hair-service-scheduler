import click

# g - unique object per request to store data.
from flask import current_app, g
from flask.cli import with_appcontext

''' # ---------------------------------
  Description:
    Gives admin privilege to an existing account

  Command:
    flask make-admin <username>

  Parameters:
    username (string)

''' # ---------------------------------
def func_make_admin(user):
  from flaskr.models import db, UserAccount, UserAccountType

  # check if user exists
  account = UserAccount.query.filter_by(username=user).first()
  if account is None:
    click.echo('Invalid user: {0}'.format(user))
    return

  # check if user already admin
  if account.type == UserAccountType.admin:
    click.echo('Account {0} already has an admin account'.format(user))
    return

  account.type = UserAccountType.admin
  db.session.commit()
  click.echo('{0} was elevated to admin privilege.'.format(user))
  return

@click.command('make-admin')
@click.option('--user', '-u', default='', help="Elevate an account to Admin privilege")
@with_appcontext
def cmd_make_admin(user):
  func_make_admin(user)


''' # ---------------------------------
  Description:
    register the command to the application instance (called from factory)

  DO NOT TOUCH!
''' # ---------------------------------
def init_app(app):
  # app.teardown_appcontext()
  app.cli.add_command(cmd_make_admin)