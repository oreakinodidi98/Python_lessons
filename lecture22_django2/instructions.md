# process

- python -m venv venv
- . .\venv\Scripts\Activate
- pip install django
- pip list
- pip freeze > requirements.txt
- **Inastal a DJANGO project ->** django-admin startproject auth_project .
- run server -> python manage.py runserver
- folder structure
  - settings.py -> settings of application
  - urls.py ->  path
- **Inastal a DJANGO app ->**django-admin startapp auth_app

## register application

- in project -> settings -> INSTALLED_APPS -> add name of application E.G auth_app

## run project

- start Project:
```py project_name.py runserver```
```python manage.py makemigrations```
```python manage.py migrate```

- add urls.py to apps folder
  - import views.py from app directory
- modify views.py in apps folder
- modify urls.py in project folder
- add models.py in app folder
- add forms.py in app folder

## set up URLs

- creat URLS.py in app folder
- import include, path
- Add a URL to urlpatterns as shown in example
- this URL will be for the APP

## creeate templates

- create templates folder in app folder
- create auth app
  - inside create partials folder -> HTML that not a full page
  - e.g. header and footer

## create forms

- in app folder create forms.py

## create views

- in app folder create views
- import forms

## URL

- import url for registration page
- import from.views

## Make migrations

- ```python manage.py makemigrations```
- ```python manage.py migrate```
- create super user
- ```python manage.py createsuperuser```
- start Project:
```py manage.py runserver```