"""
Django settings for house project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from django.contrib.messages import constants as messages
import os
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fr4+g5l#y&z0pn1-%rfe^+zs_*=ziz*0ec0x#!clk$*u9m0e79'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['house-estat.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'pages',
    'realtors',
    'listings',
    'accounts',
    'contacts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'house.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'house',
    #     'USER': 'postgres',
    #     'PASSWORD': 'Password@123',
    #     'HOST': 'localhost',
    # }
#    Production ENVIRONMENT variable for Database
  'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'ddajqltjvpuf75',
      'USER': 'adpnxpkeuwkqci',
      'PASSWORD': '41ed3ca101a605a5339a760e51eaf4e57a2d96696fd71483de3effab3a86dea0',
      'HOST': 'ec2-52-18-116-67.eu-west-1.compute.amazonaws.com',
      'PORT': '5432',
   }
#      'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': 'rcrczuqylupnym',
#       'USER': 'd6h3oudl33ioc9',
#       'PASSWORD': '94182e3b411a6a9907b3d0b062736c22d5a216e6bf1fb311a93dbbd035d4d7c0',
#       'HOST': 'ec2-52-212-228-71.eu-west-1.compute.amazonaws.com',
#       'PORT': '5432',
#    }
# TRY WITH ENVIRONMENT VARIABLES
#    'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': env('DB_NAME'),
#       'USER': env('DB_USER'),
#       'PASSWORD': env('DB_PASSWORD'),
#       'HOST': env('DB_HOST'),
#       'PORT': '5432',
#     }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'house/static')
]

# Media folder settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mohammad963yusuf@gmail.com'
EMAIL_HOST_PASSWORD = 'chfakwhkiqiokxbl'
# EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_USE_TLS = True
