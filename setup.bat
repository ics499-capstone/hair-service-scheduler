@ECHO OFF
SETLOCAL

:: install flask
ECHO Installing Flask microframework
pip install flask
ECHO ** Installing flask complete

:: install DotEnv
ECHO Installing DotEnv
pip install python-dotenv
ECHO ** Installing python-dotenv complete

:: Install flask-migrate
ECHO Installing flask-migrate
pip install flask-migrate
ECHO ** Installing flask-migrate complete

:: TODO: handle python dependencies better