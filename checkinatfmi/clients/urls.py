from django.conf.urls import patterns
from django.core.urlresolvers import resolve

# /checkin/
urlpatterns = patterns('clients.views',
    (r'status/', 'status'),
    (r'$', 'checkin'), 
)
