#  in case when i go live

from .base import *

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['ip-address', 'www.website.com']

# not commonly needed while development
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



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('db_NAME'),
        'USER': config('db_USER'),
        'PASSWORD': config('db_PASSWORD'),
        'HOST': config('db_HOST'),
        'PORT': '',
    }
}