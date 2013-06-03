from django.conf.urls import patterns
from django.core.urlresolvers import resolve

# /checkin/
urlpatterns = patterns('website.views',
    (r'$', 'index'),
    (r'$', 'statistics'),
)
