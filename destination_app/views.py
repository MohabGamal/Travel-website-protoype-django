from destination_app.forms import BookingForm
from django.shortcuts import redirect, render
from destination_app.models import  Booking, Destination, DestinationGallary
from accounts.models import Profile
from django.db.models import Count
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from destination_app.filters import DestinationFilter


# Create your views here.

'''
class DestinationsView(ListView):
    model = Destination
    #queryset = Destination.objects.all()
    template_name = 'destination/destinations.html'
    #context_object_name ='destinations' 
    paginate_by = 3

    
'''

def DestinationsView(request):
    all = Destination.objects.all().order_by('price')
    top_countries = Destination.objects.values('country').annotate(qcount=Count('country')).order_by('-qcount')[:4]
                    # group_by countries which are categories for destinations. To show how many destinations per country and order_by the highest country in destinations count (DESC)

    myfilter=DestinationFilter(request.GET,queryset=all)
    filtered_destinations=myfilter.qs                   # this line is a must for pagination  

    p = Paginator(filtered_destinations, 3)#num of items per page
    page_number = request.GET.get('page')
    #page_obj = p.get_page(page_number)

    try:
        page_obj = p.page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)                  #if page number is not intger get the first page
    except EmptyPage:
        page_obj = p.page(p.num_pages)        #if page is empty get the last page

    context ={
            'destinations' :page_obj,
            'top_countries' :top_countries,
            'myfilter'      :myfilter,
            }

    return render(request, 'destination/destinations.html',context)


def DestinationDetailsView(request, slug):
    destination_details=Destination.objects.get(slug=slug)        
    photos = DestinationGallary.objects.filter(destination=destination_details) # to show destination gallary
                                               #foreignkey field     #queryset 
    highly_rated_destinations= Destination.objects.filter(ratings__isnull=False).order_by('ratings__average')[:3]

    form=BookingForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        if not Booking.objects.get(full_name= request.user):    # if not user already booked in the travel 
            profile=Profile.objects.get(user=request.user)
            form.instance.full_name=profile
            form.instance.email= profile.user.email
            form.instance.phone_number=profile.phone_number
            form.instance.country=profile.country
            form.instance.destination=destination_details
            form.save()
        return redirect(reverse('destination:destination_details', args=(slug,)))


    context={
         'destination_details' : destination_details,
         'photos' : photos,
         'bookingform' : form,
         'highly_rated_destinations' : highly_rated_destinations,
         }
    return render(request,'destination/destination_details.html',context)


