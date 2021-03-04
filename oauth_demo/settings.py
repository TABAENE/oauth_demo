"""
Django settings for oauth_demo project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'un8rd+6v4p+rx7z*pl!m-p&cf&w(9frf=ssu4f*wmc!7w5%in4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'oauth2_provider',
    'rest_framework',
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

ROOT_URLCONF = 'oauth_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'oauth_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# OAUTH settings
# https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html
AUTH_USER_MODEL='users.User'
LOGIN_URL='/admin/login/'
ID="eM9iQSn7iT1GjQOSAjaYRww2TNf3RlM2RsdmPtn8"
SECRET="AJuLUWfAlVbblVLmfyMMTnJkBs2RIRJLkVMYVzf1Hj9vq6DhT3PaSEJ5gmn6xf4RqRWwj1E6fPiMFbqkTWJDRLcGhSSR7XRvqakE4q63HdDr5lYhdhWGn9CXAEFKrybr"
code="lxZjgcWB2c3ZGYMXxoh804FP40FK9d"

"""
Steps to get your token and use your API - 

Point your browser to http://127.0.0.1:8000/o/applications/register/ lets create an application.

Hit below URL: This identifies your application, the user is asked to authorize your application to access its resources.
http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=eM9iQSn7iT1GjQOSAjaYRww2TNf3RlM2RsdmPtn8&redirect_uri=http://127.0.0.1:8000/noexist/callback

on registration you will be redirected to below URL.
http://127.0.0.1:8000/noexist/callback?code=lxZjgcWB2c3ZGYMXxoh804FP40FK9d

Now that you have the user authorization is time to get an access token:
curl -X POST \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "client_id=eM9iQSn7iT1GjQOSAjaYRww2TNf3RlM2RsdmPtn8" \
    -d "client_secret=AJuLUWfAlVbblVLmfyMMTnJkBs2RIRJLkVMYVzf1Hj9vq6DhT3PaSEJ5gmn6xf4RqRWwj1E6fPiMFbqkTWJDRLcGhSSR7XRvqakE4q63HdDr5lYhdhWGn9CXAEFKrybr" \
    -d "code=wJ0Y9N9S0nWgQsDJyofMR0dFUfbjH8" \
    -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
    -d "grant_type=authorization_code"

curl \
    -H "Authorization: Bearer xAgIQn9MbujwB0MOEUhrgtTHToAZt4" \
    -X GET http://localhost:8000/resource
"""

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}