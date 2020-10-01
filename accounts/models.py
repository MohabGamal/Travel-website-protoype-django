from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField      # changes in settings

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image=models.ImageField(upload_to='profiles/')
    city=models.CharField(max_length=100, null=False, blank=False)
    country = CountryField(null=False , blank=False, db_index=True,   #package
    countries_flag_url='flags/{code}.gif')                         #to show flags #check out settings, base.html, static files(flags), template 
    phone_number=PhoneNumberField(null=False , blank=False)        #package  #check out settings

    def __str__(self):
        return str(self.user)



@receiver(post_save, sender=User)#SGINAL # to relate between profile & User(built in table)
def create_user_profile(sender, instance, created, **kwargs):  #create user when i create profile
    if created:
        Profile.objects.create(user=instance)





