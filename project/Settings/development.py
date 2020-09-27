#for my additions of settings

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']   # for debug toolbar


INSTALLED_APPS+=[
    #installed apps:
    'debug_toolbar',
    "bootstrap4",
    'django_countries',
    'phonenumber_field',
    'el_pagination', 
    #created apps:
    'destination_app',
]

MIDDLEWARE+=[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':config('PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}


PHONENUMBER_DB_FORMAT = 'E164'      # like: +|'country code'|'telecom code'|'phone number'
                                        #   +        2            010         22349557


COUNTRIES_FLAG_URL = 'flags/{code}.gif'         # to show flags #check out models, base.html, static files(flags), template



# debug_toolbar settings:

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True



DEBUG_TOOLBAR_CONFIG={
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'RESULTS_CACHE_SIZE': 100,   #changed from 25 to 100 to fix something
}