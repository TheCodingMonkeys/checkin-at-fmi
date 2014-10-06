from django.conf.urls import patterns, url

# /checkin/
urlpatterns = patterns('website.views',
    url(r'^$', 'index'),
    url(r'statistics/$', 'statistics'),
    url(r'profile/$', 'profile'),
    url(r'library/$', 'library'),
    url(r'show-book/(?P<book_id>[0-9]+)/$', 'show_book', name='show_book'),
)