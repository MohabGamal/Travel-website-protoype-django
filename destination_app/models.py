from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField      # changes in settings
from django.utils.text import slugify

from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.

distincit_with_choices=[
              #db name        #UI name
            ('near_beach', 'Near Beach'),
            ('near_mountain','Near Mountain'),
]


class Destination(models.Model) :
    title = models.CharField(max_length=100,)
    duration= models.PositiveSmallIntegerField(null=False)
    image= models.ImageField(upload_to='Destinations')
    description = models.TextField(max_length=1000)

    rooms = models.PositiveSmallIntegerField(null=False)
    bathrooms= models.PositiveSmallIntegerField(null=False)
    distinct_with = models.CharField(max_length=100, choices=distincit_with_choices, blank=True)

    price=models.IntegerField(null=False)
    website=models.URLField(null=True)
    slug= models.SlugField(blank=True, null=True)
    ratings = GenericRelation(Rating, related_query_name='ratings') # to query by ratings

    check_in_date=models.DateField()
    check_out_date=models.DateField()
    published_at= models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=100, null=True)

    city=models.CharField(max_length=100, null=False, blank=False)
    country = CountryField(null=False , blank=False, db_index=True,   #package
    countries_flag_url='flags/{code}.gif')                         #to show flags #check out settings, base.html, static files(flags), template 
    phone_number=PhoneNumberField(null=False , blank=False)        #package  #check out settings


    def save(self,*args, **kwargs):              #overriding save method in admin page
       self.slug= slugify(self.title)           #create a slug
       super(Destination,self).save(*args,**kwargs)


    def __str__(self):
         return self.title


class DestinationGallary(models.Model):     # to show destination photos in details # check out admin.py
    destination = models.ForeignKey(Destination, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'Destination_gallary')

    def __str__(self):
         return '{0}'.format(self.images)


class Booking(models.Model):
    full_name=models.CharField(max_length=50, default="", null=False , blank=False)
    email=models.EmailField( max_length=254, default="", null=False , blank=False)
    phone_number=PhoneNumberField(null=False , blank=False, default='' )
    destination=models.ForeignKey(Destination, on_delete=models.CASCADE, default="", null=False , blank=False)
    country = CountryField(null=False , blank=False, db_index=True,   #package
    default="", countries_flag_url='flags/{code}.gif')
    check_in_date=models.DateField( null=False , blank=False)
    check_out_date=models.DateField( null=False , blank=False)

    def __str__(self):
         return '{0}'.format(self.destination)
         
   
