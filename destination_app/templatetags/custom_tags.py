from django import template         # to create coustm template tags

register = template.Library()

@register.simple_tag
def relative_url(value, field_name, urlencode=None):    #to give the pagination the url of the page with current filters
    url = '?{}={}'.format(field_name, value)            # use this func to paginate multi-filter results
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url