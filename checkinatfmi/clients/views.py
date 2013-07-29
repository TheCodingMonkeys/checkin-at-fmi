# Create your views here.
import sys
import datetime

from django.utils.timezone import utc

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
            client.status_changed = datetime.datetime.utcnow().replace(tzinfo=utc)
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
        if client.status:
            key = request.POST.get("key", "")
            checkin_time = request.POST.get("time", "")
            print checkin_time
            try:
                user = User.objects.get(card_key = key)
            except User.DoesNotExist:
                user = User.create(key)
            active_checkins = Checkin.objects.filter(user__name = user.name, active = True)
            for active_checkin in active_checkins:
                print "CHECKOUT" + str(active_checkin) + "@" + checkin_time
                active_checkin.checkout(checkin_time)
            if not (client.place in [check.place for check in active_checkins]):
                print client.place
                Checkin.checkin(user, client.place, checkin_time)
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404
