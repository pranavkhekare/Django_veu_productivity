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
  * Login screen suing email
1. Provided features for filtering the created user on admin screen
1. Created User profile to add additional features for each created user
  * Used OnetoOne to link User profile model with User model created before.
  
  
  

## Tables (DB: sqlite3)
* Tasks
* Users
* User_profiles
