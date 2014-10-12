from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from identifications.models import Book
from identifications.models import Cardowner

from models import LendRequest


@login_required
def request(request):
    book = Book.objects.get(pk=int(request.GET.get('book')))
    cardowner = Cardowner.objects.get(user=request.user)
    lendRequest = LendRequest.objects.get_or_create(requester=cardowner, book=book)[0]
    lendRequest.status = LendRequest.WAITING
    lendRequest.save()

    return HttpResponse(status=200)
