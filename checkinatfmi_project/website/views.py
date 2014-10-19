from datetime import datetime, timedelta, time
from dateutil.relativedelta import relativedelta

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.db.models import Q

from utils.datetime_util import days_hours_minutes

from activities.models import Checkin, Borrow
from university.models import Place, Specialty
from identifications.forms import BookSerachFrom
from identifications.models import Book
from lends.models import LendRequest

def index(request):
    now = datetime.now()
    places = Place.objects.all()
    all_places = []
    for place in places:
        checkins_inside = Checkin.checkins.active().order_by('-checkin_activity__time')
        all_users = []
        for checkin in checkins_inside:

            all_users += [
                    {
                        'first_name': checkin.cardowner.user.first_name,
                        'last_name': checkin.cardowner.user.last_name,
                        'active_time': days_hours_minutes(checkin.active_time())
                    }
            ]
        all_places += [[place, place.capacity, len(all_users), all_users]]

    return render(request, 'index.html', locals())

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
        for i in reversed(xrange(12)):
            date = today_date + relativedelta(months=i-11)
            monthly_checkins += [
                Checkin.checkins.filter_by_place_and_month(
                    place,
                    today_date.month - i
                ).count()
            ]

        daily_checkins = []
        for i in reversed(xrange(7)):
            daily_checkins += [
                Checkin.checkins.filter_by_place_day_and_month(
                    place,
                    (today_date - timedelta(days=i)).day,
                    today_date.month
                ).count()
            ]

        checkins_for_today = Checkin.checkins.filter_by_place_day_and_month(
                place,
                today_date.day,
                today_date.month)

        hourly_checkins = [0]*24
        for checkin in checkins_for_today:
            hourly_checkins[checkin.checkin_activity.time.hour] += 1

        specialties = Specialty.objects.all()
        piechart_specialty = []
        for specialty in specialties:
            piechart_specialty += [
                    {
                    'specialty': specialty,
                    'checkin_counts':
                    Checkin.checkins.filter_by_place_and_specialty(
                        place,
                        specialty
                    ).count()
                }
            ]

        piechart_grade = []
        for grade in range(4):
            piechart_grade += [
                {
                    'grade': grade,
                    'checkin_counts':
                    Checkin.checkins.filter_by_place_and_grade(
                        place,
                        grade + 1
                    ).count()
                }
            ]

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

    return render(request, 'statistics.html', locals())


@login_required
def profile(request):
    return render(request, 'profile.html', locals())


def library(request):
    form = BookSerachFrom(request.GET if request.GET else None)

    if form.is_valid():
        books = Book.objects.filter(
                    Q(title__contains=form.cleaned_data['search']) | 
                    Q(author__contains=form.cleaned_data['search']) |
                    Q(publisher__contains=form.cleaned_data['search'])
                )

        if form.cleaned_data['from_year'] and form.cleaned_data['to_year']:
            books = books.filter(year__range=(
                form.cleaned_data['from_year'],
                form.cleaned_data['to_year'])
            )

    return render(request, 'library.html', locals())


def show_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book_borrowed = Borrow.objects.filter(
        handback__isnull=True,
        borrower=request.user.cardowner
    )
    book_lended = LendRequest.objects.filter(
        book=book,
        requester=request.user.cardowner
    )

    return render(request, 'show_book.html', locals())


@login_required
def books_to_return(request):
    borrows = Borrow.objects.filter(
        handback__isnull=True,
        borrower=request.user.cardowner
    )

    books = set(map(lambda x: x.borrow.carrier.identification, borrows))
    return render(request, 'books_to_return.html', locals())
