import sys
import datetime
import urllib2
import json

from django.utils.timezone import utc

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from activities.models import Checkin, Borrow
from activities.views import register_activity
from identifications.models import Book
from models import Client
from university import helper as university_helper
from university.models import Place


@csrf_exempt
@require_http_methods(['POST'])
def status(request):
    """
    Updates clients status and returns if they have the privilages to send
    """
    mac = request.POST.get("mac", "")
    client = Client.objects.get_or_create(mac = mac)[0]

    if client.status == False:
        return HttpResponse(status=401)

    client.status_changed = datetime.datetime.now()
    client.save()
    return HttpResponse(status=200)


@csrf_exempt
@require_http_methods(['POST'])
def checkin(request):
    """
    Checkin request -> asks checks
    """
    mac = request.POST.get("mac", "")
    key = request.POST.get("key", "")
    time = request.POST.get("time", "")

    client = Client.objects.get_or_create(mac = mac)[0]
    if not client.status:
        return HttpResponse(status=401)

    return register_activity(request, time=time, data=key, client=client)
