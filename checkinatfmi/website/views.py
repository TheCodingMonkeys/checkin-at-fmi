from datetime import datetime, timedelta, time

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from django.shortcuts import render_to_response
from django.template import RequestContext


from checkin.models import Checkin
from places.models import Place
from university.models import User


def days_hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60, td.seconds % 60


def index(request):
    now = datetime.now()
    places = Place.objects.all()
    all_places = []
    for place in places:
        checkins_inside = Checkin.objects.filter(place = place, active = True)
        all_users = []
        for checkin in checkins_inside:
            print checkin.checkin_time
            all_users += [{'first_name': checkin.user.first_name, 'last_name': checkin.user.last_name,
                            'active_time': days_hours_minutes(now-checkin.checkin_time)}]
            print (now-checkin.checkin_time)
        all_places += [[place, place.capacity, len(all_users), all_users]]
    print all_places
    return render_to_response('index.html',
            {
                "places" : all_places,
            },
            context_instance=RequestContext(request))

def statistics(request):
    place_checkins_by_hour = []

    places = Place.objects.all()
    for place in places:    
        today = datetime.now.date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        place_checkins_by_hour += [
            {
                'place': place,
                'count': Checkin.objects.filter(place = place, checkout_time__day=today.day).count,
            }
        ]

    return render_to_response('statistics.html',
            {
                "place_checkins_by_hour" : place_checkins_by_hour,
            },
            context_instance=RequestContext(request))


@login_required
def profile(request):
    all_users = User.objects.all()

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('profile.html',
            {
            },
            context_instance=RequestContext(request))
        else:
            pass
            # Return a 'disabled account' error message
    else:
        pass
        # Return an 'invalid login' error message.

    
