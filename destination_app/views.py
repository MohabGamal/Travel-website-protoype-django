from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from . models import Destination, DestinationGallary
from django.db.models import Count
from django.core.paginator import Paginator


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
    p = Paginator(all, 3)#num of items per page
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context ={'destinations' :page_obj,'top_countries' :top_countries}
    return render(request, 'destination/destinations.html',context)




def DestinationDetailsView(request, slug):
    destination_details=Destination.objects.get(slug=slug)
                                         #foreignkey field     #queryset         
    photos = DestinationGallary.objects.filter(destination=destination_details) # to show destination gallary
    context={'destination_details' : destination_details, 'photos' : photos,}
    return render(request,'destination/destination_details.html',context)


