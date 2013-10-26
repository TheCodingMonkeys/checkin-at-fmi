import datetime

from django.utils.timezone import utc
from django.shortcuts import render_to_response
from django.template import RequestContext

from checkin.models import Checkin
from places.models import Place
from users.models import User


def days_hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60, td.seconds % 60


def index(request):
    now = datetime.datetime.now()
    places = Place.objects.all()
    all_places = []
    for place in places:
        checkins_inside = Checkin.objects.filter(place = place, active = True)
        all_users = []
        for checkin in checkins_inside:
            print checkin.checkin_time
            all_users += [[checkin.user.first_name, days_hours_minutes(now-checkin.checkin_time)]]
            print (now-checkin.checkin_time)
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
        checkin_count = Checkin.objects.filter(user__first_name = user.first_name).count()
        scores += [[user.first_name, checkin_count]]

    print scores
    return render_to_response('statistics.html',
            {
                "scores" : scores,
            },
            context_instance=RequestContext(request))
