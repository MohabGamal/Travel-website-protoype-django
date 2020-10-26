import django_filters
from django_filters.filters import DateFromToRangeFilter, RangeFilter
from destination_app.models import Destination

class DestinationFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    price=RangeFilter()
    check_in_date=DateFromToRangeFilter()
    class Meta:
        model = Destination
        fields = ('check_in_date','price', 'description')
        #exclude=()