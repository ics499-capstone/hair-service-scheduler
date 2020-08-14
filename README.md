# ICS-499 Software Engineering Capstone
## Hair Service Application
[![Build Status](https://travis-ci.org/ics499-capstone/hair-service-scheduler.svg?branch=master)](https://travis-ci.org/ics499-capstone/hair-service-scheduler)

### About
This is an application that hosts a variety of services for hair service admins.
- Language: Python (version 3.8.0)
- Framework: Flask
- Persistence: SQLite
- Industry: Hair
- Frontend: React

### Working with the Backend (API)
- Download [Python 3.8.0](https://www.python.org/downloads/release/python-380/)
- Download [SQLite Browser](https://sqlitebrowser.org/dl/) to view the DB
- Ensure Python is Downloaded
  - `> python --version`
- Install python dependencies
  - `> setup`
- To Run the application
  - `> flask run`
  - Navigate to browser go to `localhost`
  
### Migrations
- ```flask db init```
- ```flask db migrate -m <msg>```
- ```flask db upgrade```

### Make flask project
- ```pip install --editable .```

### Run tests
- ```pytest -v```

### Custom commands:
- ```flask make-admin -u <username>```
  - To elevate an account to Admin privilege

### Continuous Integration
- [travis](https://travis-ci.org/github/ics499-capstone/hair-service-scheduler)

## Contributing
- Visit the [Iteration Board](https://github.com/ics499-capstone/hair-service-scheduler/projects/1)
- Pick out a task in the "To do" Column
- When working on a ticket, please commit the ticket number onto the commit message