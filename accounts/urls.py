
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup, name='signup'),
    path('profile/<str:user>/',views.profile, name='profile'),   # the user field in Profile model
    path('profile/<str:user>/edit',views.profile_edit, name='profile_edit'),
    
              ]




