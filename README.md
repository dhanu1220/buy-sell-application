## What is Django
Django is a Python framework that makes it easier to create web sites using Python.
It allows us to build any kind of scalable and complex web application from scratch
which could be accessed by thousands of people
## Virtualenv
Virtualenv allows easy management of dependencies and avoids conflicts between different versions of libraries and packages.
### Creating virtualenv
To create a virtual environment, run `virtualenv env`. Activate the virtualenv from the script using `.\env\Scripts\activate` on Windows or `source env/bin/activate` on macOS and Linux.
## Installing Django
```
pip install django
```
## Running app on local server
**On windows**
```
python manage.py runserver
```
**On mac**
```
python3 manage.py runserver
```
## Django ORM
Django’s Object-Relational Mapping (ORM) system, is a bridge between the database and the application’s code.</br>
Django’s ORM is essentially a pythonic technique to build SQL to query and edit your database and obtain results.
## Django shell
Django shell allows us to save, update and retrieve our models in our code. Interacting with databases while working with projects in production is very essential and unavoidable.
```
python manage.py shell
```
