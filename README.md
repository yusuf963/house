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

## Postgresql
if you are in mac
`brew install postgresql`
if you are in windows
`https://www.postgresql.org/download/`
install DBeaver

install postgresf driver
https://jdbc.postgresql.org/download.html
POstgress command line client
https://www.postgresql.org/download/linux/ubuntu/
`$ brew services start postgresql # or "brew services run postgresql" to have it not restart at boot time`
`psql postgres`
`brew search postgres`
`\l`
## you might cross role dons't excit, run the following to create a user
`/opt/homebrew/bin/createuser -s postgres` form M1

`/usr/local/opt/postgres/bin/createuser -s postgres`
`/usr/local/opt/postgresql/bin/createuser -s postgres`
`/usr/local/opt/postgresql@11/bin/createuser -s postgres`


## Migrate to postgres
1. create a database on Dbeaver
2. keep the username, password, and hostname the handy
3. in the seeting.py change the default database to postgres it should look lis this
` DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'house',
        'USER': 'postgres',
        'PASSWORD': 'Password@123',
        'HOST': 'localhost',
    }
}
`
4. install packages to help you communicate with the database
`pip install psycopg2`
`pip install psycopg2-binary`
5. run the migrate command
`python manage.py migrate`
6. make sure your Django app interact with the database

## Make Migration
1. make your models/schema in you models files in each app, e.g (listings/models.py, realtors/models.py)
2. if you are using uploadphoto field, you need to add pillow as dependency
`pip install pillow` or `python -m pip install Pillow`
3. run the command below to make a migration
`python manage.py makemigrations`
    a. you will notice a file called `0001_initial.py` in each app
    b. this file will contain the schema of the database
    c. you can see the schema in the file
    d. (Optional), run the command below to see the sql code
    `python manage.py sqlmigrate listings 0001`

