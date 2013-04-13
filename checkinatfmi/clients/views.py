# Create your views here.
import sys

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ObjectDoesNotExist

from models import Client

# TODO csrf hack -> needs to identify client
@csrf_exempt
def status(request):
    """
    Checkin request
    """
    if request.method == 'GET':
        return HttpResponse("Sorry man ;)")    
    elif request.method == 'POST':
        mac = request.POST.get("mac", "")
        try:
            client = Client.objects.get(mac = mac)
        except ObjectDoesNotExist, e:
            client = Client()
            client.mac = mac
            client.save()
        
        if client.status == True:
            return HttpResponse("ok")
        else:
            return HttpResponse("error")

# TODO csrf hack -> needs to identify client
@csrf_exempt
def checkin(request):
    """
    Checkin request
    """
    if request.method == 'GET':
        return HttpResponse("Sorry man ;)")    
    elif request.method == 'POST':
        return HttpResponse("%s chacked in" % str(id_number))
