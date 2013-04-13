from django.http import HttpResponse
from django.http import Http404

def index(request):
    return HttpResponse("Pandichki!")
