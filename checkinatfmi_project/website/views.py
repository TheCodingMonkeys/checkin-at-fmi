from datetime import datetime, timedelta, time
from dateutil.relativedelta import relativedelta

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from django.shortcuts import render_to_response
from django.template import RequestContext

from activities.models import Checkin
from university.models import Place, Specialty


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

def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def statistics(request):
    place_checkins = []

    places = Place.objects.all()
    for place in places:    
        today_date = datetime.now().date()

        monthly_checkins = []
        for i in range(12):
            date = today_date + relativedelta(months=i-11)
            monthly_checkins += [Checkin.objects.filter(place = place, checkin_time__month=date.month).count()]

        daily_checkins = []
        for i in range(7):
            daily_checkins += [Checkin.objects.filter(place = place, checkin_time__day=(today_date + timedelta(days=i-6)).day).count()]

        
        checkins_for_today = Checkin.objects.filter(place = place, checkin_time__year=today_date.year,
                                                                    checkin_time__month=today_date.month,
                                                                    checkin_time__day=today_date.day)

        hourly_checkins = [0]*24
        for checkin in checkins_for_today:
            hourly_checkins[checkin.checkin_time.hour] += 1

        specialties = Specialty.objects.all()
        piechart_specialty = []
        
        for specialty in specialties:
            piechart_specialty += [{'specialty': specialty,
                                    'checkin_counts': Checkin.objects.filter(place = place,
                                                        user__specialty=specialty).count()}]


        piechart_grade = []

        for grade in range(4):
            piechart_grade += [{'grade': grade,
                                    'checkin_counts': Checkin.objects.filter(place = place,
                                                        user__grade=grade).count()}]

        place_checkins += [
            {
                'place': place,
                'monthly_checkins': monthly_checkins,
                'daily_checkins': daily_checkins,
                'hourly_checkins': hourly_checkins,
                'piechart_specialty': piechart_specialty,
                'piechart_grade': piechart_grade,
            }
        ]

        

    return render_to_response('statistics.html',
            {
                'place_checkins': place_checkins,
            },
            context_instance=RequestContext(request))


@login_required
def profile(request):

    return render_to_response('profile.html',
    {

    },
    context_instance=RequestContext(request))

@login_required
def library(request):
    return render_to_response('library.html',
    {

    },
    context_instance=RequestContext(request))

    