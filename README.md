
# Setup and run run the project locally
## install the packages inside requirement.txt
`pip install -r requirements.txt`
## Run virtual env
`virtualenv -p python3.8 .`
## Install Django
`pip install Django==4.0.3`
## Check Django version
 `python -m django --version`
## Create Django Project
 `django-admin startproject marketplace`
## Run django 
`python manage.py runserver`
## Create a new Django app
`django-admin startapp marketplace`
## create a superuser
`python manage.py createsuperuser` 
## uninall all the unwanted python packages 
`pip uninstall -y -r <(pip freeze)`
## collect static
`python manage.py collectstatic`






work process
## work on static/html template:
1. Create a static folder in the project directory, and register the path in settings.py 
2. create a templates folder in the root directory
3. add the html file to the template folder
4. register the template folder in the settings.py template section 
5. break your html file into multiple html files/ footer/ nav/ sections
6. mark the html file always with {% load static %}, and the sub component with {% include 'filename.html' %} 
7. change the path of the static files in the html file like {% static 'css/style.css' %} instead of 'asset/css/style.css'
## Make sure:
1. the html file is in the templates folder
2. all paths are correctly pointing the  the right folder/file
3. run the command below to check to collect static
`python manage.py collectstatic`
 a. this will collect all the static files in the static folder in the root directory

4. for src tag you use {% static 'css/style.css' %} instead of 'asset/css/style.css'
5. for href tag you use {% url 'index' %} instead of href='/index.html'