# Create your views here.
import sys
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from models import Client
from users.models import User
from places.models import Place
from checkin.models import Checkin

# TODO csrf hack -> needs to identify client
@csrf_exempt
def status(request):
    """
    Updates clients status and returns if they have the privilages to send
    """
    if request.method == 'POST':
        mac = request.POST.get("mac", "")
        try:
            client = Client.objects.get(mac = mac)
        except ObjectDoesNotExist, e:
            client = Client()
            client.mac = mac
            client.save()
         
        if client.status == True:
            client.status_changed = datetime.now
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404

# TODO csrf hack -> needs to identify client
@csrf_exempt
def checkin(request):
    """
    Checkin request -> asks checks
    """
    if request.method == 'POST':
        mac = request.POST.get("mac", "")
        try:
            client = Client.objects.get(mac = mac)
        except ObjectDoesNotExist, e:
            print "client doesn't exist"
            return HttpResponse("error")
        if client.status:# and client.is_updated():
            # Checkin
            key = request.POST.get("key", "")
            try:
                user = User.objects.get(card_key = key)
                place = Place.objects.get(mac = mac)          
            except ObjectDoesNotExist, e:
                return HttpResponse("error")

            checkin_time = request.POST.get("time", "")

            Checkin.checkin(user, place, checkin_time) 

            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404
