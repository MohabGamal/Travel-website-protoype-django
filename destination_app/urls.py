from django.urls import include , path
from . import views

app_name='destination_app'

urlpatterns = [
    path('', views.DestinationsView, name='destinations'),

    path('<str:slug>', views.DestinationDetailsView, name='destination_details'),  #must be the last path in case i have an url matchs with slug the browser will go to the url not the slug
    
    
    


]
