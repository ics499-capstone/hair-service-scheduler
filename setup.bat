@ECHO OFF
setlocal enabledelayedexpansion

  :: install dependencies
  ECHO ** Installing Python dependencies
  pip install -r requirements.txt
  ECHO ** Installation complete

  :: set variables
  ECHO ** Setting Environment variables
  SET "FLASK_APP=flaskr" & echo FLASK_APP=!FLASK_APP!
  SET "FLASK_ENV=development" & echo FLASK_ENV=!FLASK_ENV!
  SET "SQLALCHEMY_DATABASE_URI=sqlite:///app.db" & echo FLASK_ENV=!SQLALCHEMY_DATABASE_URI!
  ECHO ** Environment variables setted!
  
  :: install the projext
  ECHO ** Installing the project **
  pip install -e .
  ECHO ** Installation complete

endlocal