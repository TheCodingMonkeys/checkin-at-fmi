from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import helper
from models import Activity, Carrier


@csrf_exempt
def register_activity(request, time='', data='', client=''):
    carrier, created = Carrier.objects.get_or_create(data=data) 
 
    if carrier.is_registered():
        Activity.create(time, client, carrier)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)

