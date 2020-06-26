# Virtual Environment Variables
#
# To get Environment Variables from python source codes:
# `import os`
# `os.environ['THE_DESIRE_ENV_VAR']`

# enables dynamically updates of website
FLASK_ENV=development

# defaults to localhost
FLASK_RUN_HOST=localhost

# sets the port to 80
FLASK_RUN_PORT=80

# using SQLite
SQLALCHEMY_DATABASE_URI=sqlite:///app.db

# signal flask everytime database changes (development purposes)
SQLALCHEMY_TRACK_MODIFICATIONS=True