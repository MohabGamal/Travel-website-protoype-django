#for my additions of settings

from .base import *

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS+=[
    #'debug_toolbar'
]

MIDDLEWARE+=[
    #debug_toolbar
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'leesinvarus1',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# debug_toolbar settings:
