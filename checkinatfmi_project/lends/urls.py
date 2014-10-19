from django.conf.urls import patterns, url

urlpatterns = patterns('lends.views',
    url(r'request/$', 'request'),
    url(r'cancel-request', 'cancel_request')
)
