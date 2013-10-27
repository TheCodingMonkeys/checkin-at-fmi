import sys
import datetime
import urllib2
import json

from django.utils.timezone import utc

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from models import Client
from university.models import CustomUser, Book
from places.models import Place
from checkin.models import Checkin, Bookrent

FMI_LIBRARY_URL = "http://zala100.sofiapubcrawl.com/API.php"

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
            client.status_changed = datetime.datetime.now() #.utcnow().replace(tzinfo=utc)
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        raise Http404

@csrf_exempt
def checkin(request):
    """
    Checkin request -> asks checks
    """
    if request.method != 'POST':
        return HttpResponse("error")
    mac = request.POST.get("mac", "")
    try:
        client = Client.objects.get(mac = mac)
    except ObjectDoesNotExist, e:
        print "client doesn't exist"
        return HttpResponse("error")
    if not client.status:
        return HttpResponse("error")
    
    key = request.POST.get("key", "")            
    checkin_time = request.POST.get("time", "")

    try:
        users = CustomUser.objects.filter(card_key = key).all()
        if len(users) > 1:
            return HttpResponse("error")
        elif len(users) == 0:
            raise CustomUser.DoesNotExist()
        
        user = users[0]
        if not user.valid:
            return HttpResponse("error")

        active_checkins = Checkin.objects.filter(user__first_name = user.first_name , active = True)
        for active_checkin in active_checkins:
            active_checkin.checkout(checkin_time)
        if not (client.place in [check.place for check in active_checkins]):
            print client.place
            Checkin.checkin(user, client.place, checkin_time)
        return HttpResponse("ok")

    except CustomUser.DoesNotExist:
        response = getBootForId(key)
        if not response:
            CustomUser.create(key)

            return HttpResponse("error")
        else:
            print response

            book_data = json.load(response) #.read()
            #book_obj = json.load(book_data)
            print book_data
            book, created = Book.objects.get_or_create(id=book_data['id'])
            title = book_data['title']
            print title
            book.title = 'Title'
            book.save()
            rent = Bookrent.bookrent(client.place, book, checkin_time)
            print book
            print rent
            #Bookrent.rent()
            return HttpResponse("ok")


def getBootForId(book_id):
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    url = urllib2.Request(FMI_LIBRARY_URL + '?code=' + str(book_id))
    try:
        request = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        return False
        
    return request