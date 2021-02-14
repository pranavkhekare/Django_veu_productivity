# Productivity tool build on Django and Veu.JS

## Running locally
1. Clone this repo
1. cd into this repo
1. Create a python virtual environment: `python -m venv venv`
1. Activate virutal environment: `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. `python manage.py runserver`

## Roadmap
### Version 1.0
1. Build backend base using Django 3
1. Created new api for getting tasks with title and description

### Version 1.1
1. Build on the previous version to add custom user logging with UserManager
1. Addded auth
    * Login screen using email
1. Provided features for filtering the created user on admin screen
1. Created User profile to add additional features for each created user
    * Used OnetoOne to link User profile model with User model created before.
    
### Version 1.2
1. Cleaned up code by creating apps directory to store all the created apps
1. Created Lists app and linked it to the user app
1. Created Lists Item app and linked it to the Lists app
1. Connected Task, Lists app using the Primary key Foreign key connection (One to One) with the User model
1. Installed nested URL app `pip install drf_nested_routers` to provide nested URL feature in Django rest framework (used for Lists & List items app)
1. Changed Sqlite DB to Postgres DB
  
  
  

## Tables (DB: sqlite3)
* Tasks
* Users
* User_profiles
* Lists
* List_items
