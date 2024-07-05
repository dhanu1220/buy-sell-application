# Django E-commerce Application
### Description 
This is a simple eCommerce website built with Django, designed for buying and selling products.User needs to create an account on our website to sell products and to proceed with the payment section.</br></br>
**Tech Stack** - Django, Tailwind CSS, SQLite3
## Features
* Browse and search for products available for sale.</br>
* Create profiles for buyers and sellers with personal information and order history.</br>
* User authentication and authorization to ensure secure access.</br>
* Process payments securely using Stripe.</br>
* Sellers can manage their products.
     * Create, edit, and delete products.
     * View a list of their specific products.
# Installation
## Creating virtualenv
To create a virtual environment, run `virtualenv env`. Activate the virtualenv from the script using `.\env\Scripts\activate` on Windows or `source env/bin/activate` on macOS and Linux.
## Installing Django
```
pip install django
```
## Django ORM
Django’s Object-Relational Mapping (ORM) system, is a bridge between the database and the application’s code.</br>
Django’s ORM is essentially a pythonic technique to build SQL to query and edit your database and obtain results.
##### Creating Migrations
```bash
python manage.py makemigrations
```
##### Applying Migrations
```bash
python manage.py migration
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
