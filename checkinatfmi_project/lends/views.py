from datetime import date
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from identifications.models import Book
from identifications.models import Cardowner

from models import LendRequest


@login_required
def request(request):
    today = date.today()

    if len(LendRequest.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)) >= 10:
        return HttpResponse(status=403)

    book = Book.objects.get(pk=int(request.GET.get('book')))
    cardowner = Cardowner.objects.get(user=request.user)

    lend_request = LendRequest()
    lend_request.requester = cardowner
    lend_request.book = book
    lend_request.status = LendRequest.WAITING

    lend_request.save()

    return HttpResponse(status=200)


@login_required
def cancel_request(request):
    book = Book.objects.get(pk=int(request.GET.get('book')))
    cardowner = Cardowner.objects.get(user=request.user)

    lend_request = LendRequest.objects.filter(requester=cardowner, book=book, status=LendRequest.WAITING).order_by('-date')[0]
    print lend_request
    print 'babami'

    lend_request.status = LendRequest.CANCELED
    lend_request.save()

    return HttpResponse(status=200)
