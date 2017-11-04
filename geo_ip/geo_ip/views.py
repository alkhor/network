from django.http import HttpResponse
import datetime
from ipware.ip import get_ip

#date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

#get_ip with usgi and reverce proxy
def get_client_ip_1(request):
    print(request)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(ip)

#get_ip using django-ipware-1.1.6
def get_client_ip_2(request):
    ip = get_ip(request)
    if ip is not None:
        return HttpResponse("we have an IP address for user there is" + ip)
    else:
        return HttpResponse("we don't have an IP address for user")
