from django.conf.urls import patterns, url
from django.core.urlresolvers import resolve

urlpatterns = patterns('activities.views',
    url(r'register/', 'register_activity', name='register_activity'), 
)
