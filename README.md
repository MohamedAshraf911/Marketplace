# Marketplace (Django-Python)
This is a project for the parallel and distributed system course where we make an online market place in which users can add, edit and delete items for other users to buy 

## Login
![FunFactory](./images/Picture1.png "FunFactory") *FunFactory*

## Installation on Windows
1. Clone this project
2. install python virtual environment 
```
pip install virtualenv
```
3. create new virtual environment
```
python -m venv venv
```
4. activate the new virtual
```
.\venv\Scripts\activate
```
5. install django localy in venv
```
pip install django 
```
6. install pillow package
```
pip install pillow
```
7. install django rest frame work
```
pip install djangorestframework
```
8. make migrations 
```
python manage.py makemigrations
```
9. apply migrations
```
python manage.py migrate
```
10. run server
```
python manage.py runserver
```
## Admin Set-Up
1. Create Super user:
```
python manage.py createsuperuser
```
2. Enter username,mail , password 
3. run server
4. go to 127.0.0.1:8000/admin 
