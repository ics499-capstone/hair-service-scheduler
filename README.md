# ICS-499 Softare Engineering Capstone
## Hair Service Application
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

### Custom commands:
- ```flask make-admin <username>```
  - To elevate an account to Admin privilege

## Contributing
- Visit the [Iteration Board](https://github.com/ics499-capstone/hair-service-scheduler/projects/1)
- Pick out a task in the "To do" Column
- When working on a ticket, please commit the ticket number onto the commit message