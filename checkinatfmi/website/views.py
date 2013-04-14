import datetime

from django.utils.timezone import utc
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from checkin.models import Checkin
from places.models import Place
from users.models import User

def index(request):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    places = Place.objects.all()
    all_places = []
    for place in places:
        checkins_inside = Checkin.objects.filter(place = place)
        all_users = []
        for checkin in checkins_inside:
            all_users += [[checkin.user.name, (now-checkin.time).days * 24 * 60]]
        all_places += [[place, place.capacity, len(all_users), all_users]]
    print all_places
    return render_to_response('index.html',
            {
                "places" : all_places,
            },
            context_instance=RequestContext(request))

def statistics(request):
    all_users = User.objects.all()
    scores = []
    for user in all_users:
        checkin_count = Checkin.objects.filter(user__name = user.name).count()
        scores += [[user.name, checkin_count]]
    
    print scores
    return render_to_response('statistics.html',
            {
                "scores" : scores,
            },
            context_instance=RequestContext(request))
