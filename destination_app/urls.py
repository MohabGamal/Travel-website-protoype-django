from django.urls import include , path
from . import views

app_name='destination_app'

urlpatterns = [
    path('',views.destinations, name='destinations'),


]