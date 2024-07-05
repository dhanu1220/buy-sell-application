## Django E-commerce Application
### Description 
This is a simple eCommerce website built with Django, designed for buying and selling products.
## Features
Product Listings: Browse and search for products available for sale.
User Profiles: Create profiles for buyers and sellers with personal information and order history.
Secure Authentication: User authentication and authorization to ensure secure access.
Payment Integration: Process payments securely using Stripe.
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
