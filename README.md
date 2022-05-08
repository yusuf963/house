
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
## collect all teh installed packages
`pip freeze > requirements.txt`






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


## •••••••••• create a database •••••••••••••
## Migrate to postgres
1. create a database on DBeaver
2. keep the username, password, and hostname the handy
3. in the seeting.py change the default database to postgres, it should look lis this
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
5. run the command below to make a migration
`python manage.py makemigrations`
6. run the migrate command
`python manage.py migrate`
7. make sure your Django app interact with the database by looking at the database

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
4. to add the new schema/table/models  to the database run the command
`python manage.py migrate`


## •••••••••• create Superuser •••••••••••••
1. create a superuser
2. run the command below to create a superuser
`python manage.py createsuperuser`
3. you will be asked for the username, email, and password
4. enter the username, email, and password
5. you will be asked to confirm the password
6. enter the password again



## •••••••••• Load data from DB to html templates •••••••••••••
1. in app/views.py import your models from .models
2. create a variable with value as Listing.objects.all()  // to fetch all data from that table
3. in the return render(request, 'listings/listings.html', {'listings': listings}) or something like this
    `
    def index(request):
        listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
        context = {
            'listings': listings
        }
        return render(request,'templates/listings/listings.html', context)
        `
3. in the html template, use the variable to display the data
4. use Jinga syntax to display the data like

`{{%if listings%}}
{% for listing in listings %}
    <h2>{{ listing.title }}</h2>
    <h3>{{ listing.price }}</h3>
    <p>{{ listing.description }}</p>
{% endfor %}
{{% else %}}
    <h2>No Listings Found</h2>
{{% endif %}}`

5. (optional) you can use humanize for better human reading
   a. register the humanize package in the settings.py
    b. mark the template with {% load humanize %}
    c. use the function like
    `{{listing.list_date|date:"d M Y"}}`
    `<h3>{{ listing.price | intcomma }}</h3>`
    `{{listing.list_date|date:"F j, Y"}}`

https://github.com/jazzband/dj-database-url
## •••••••••• Dealing with Environment variable •••••••••••••

https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f


## •••••••••• Deployments •••••••••••••
## Officail Deployment docs on aws Elasticbeanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

##Prerequisites
1. Python 3.7 or later
2. pip
3. virtualenv
4. awsebcli , in your terminal type `pip install awsebcli` to install awsebcli/make sure this in not in the virtual environment

- get your credentials from aws


## •••••••••• Deployments to Heroku •••••••••••••

4. install gunicorn
`pip install gunicorn`
5. add this line to your project/urls.py
`from django.contrib.staticfiles.urls import staticfiles_urlpatterns`
`urlpatterns += staticfiles_urlpatterns()` # this is to make the static files available in the heroku
5. in the root directory of your project, create Procfile 
`touch Procfile`
5. add the folowing to it 
`web: gunicorn myappname.wsgi`
6. in the root directory create file runtime.txt
`touch runtime.txt`
7. specify the version of python you like during runtime as Heroku by default will install 3.10.0 
`python-3.8.9` # its very case sensitive, careful
8. in you venv run the command 
`pip freeze > requirements.txt`

1. create Heroku account

2. install heroku cli
`pip install heroku`
https://devcenter.heroku.com/articles/heroku-cli
3. connect to heroku
`heroku login` # you will be asked for your username and password
.  check if you are connected to heroku
`heroku auth:whoami`
`heroku auth:token`
`heroku authorizations`
`heroku authorizations:info 059ed27c-d04a-4349-9dba-83a0169277ae`
`heroku apps`
`heroku maintenance:on` # to put the app in maintenance mode
`heroku run python manage.py createsuperuser` # to create a superuser
. after a success login, you will see the following
`heroku create` # this will initialize a new heroku app, you can se it in the web browser of your heroku account
`git add .` and `git commit -m "initial commit"`
`git push heroku master` # this will push the code to heroku or `git push heroku HEAD:master`
. Useful heroku commands
`heroku open` # this will open the heroku app in the browser
`heroku logs` # this will show the logs of the heroku app
`heroku ps` # this will show the processes of the heroku app
`heroku ps:scale web=1` # this will scale the web process to 1
`heroku buildpacks:clear`
`heroku buildpacks:add --index heroku/python`
`heroku create --region eu` # this will create a heroku app in the eu region
`heroku plugins:install heroku-fork`
`heroku fork --from sleepy-earth-90185 --to targetapp --region eu`
`heroku config:set DISABLE_COLLECTSTATIC=1` # to disable collectstatic

## change app regin if needed
`heroku plugins:install heroku-fork` 
`heroku fork --from sourceapp --to targetapp --region eu`

## Why am I seeing "Application Error"?
`heroku logs --tail --app your_app_name` # this will show the logs of the heroku app
`heroku restart` # this will restart the heroku app
`git rm he`

. add your app url to the allowd host in settings.py
`ALLOWED_HOSTS = ['my-django-app.herokuapp.com']`

https://devcenter.heroku.com/articles/python-support#specifying-a-python-version
https://devcenter.heroku.com/articles/django-app-configuration

Login to your Heroku dashboard and open your projects.
Go to Settings.
Delete heroku/python from the list of buildpacks
Then click Add buildpack → Choose "Python" → Save Changes.
Activate your environment in your code.
Run heroku ps:scale web=1.
And you're done!


https://realpython.com/django-hosting-on-heroku/
https://www.youtube.com/watch?v=lid-aICtbCI&t=576s
https://www.youtube.com/watch?v=v7xjdXWZafY
https://www.youtube.com/watch?v=GMbVzl_aLxM