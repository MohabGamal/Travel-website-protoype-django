from django.contrib import admin
from .models import Destination, DestinationGallary, Booking

#admin.site.register(Destination)
admin.site.register(DestinationGallary)
admin.site.register(Booking)

class DestinationGallaryAdmin(admin.StackedInline):
    model = DestinationGallary
 
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestinationGallaryAdmin]         # to inline two models as one and give ability to upload more than one file
 
    class Meta:
       model = Destination
 
'''@admin.register(DestinationGallary)
class DestinationGallaryAdmin(admin.ModelAdmin):
    pass'''