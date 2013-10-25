from django.contrib import admin

from models import Checkin

class CheckinAdmin(admin.ModelAdmin):
    fields = ['user', 'place', 'checkin_time', 'checkout_time', 'active']
    list_display = ['user', 'place', 'checkin_time', 'checkout_time', 'active']

admin.site.register(Checkin, CheckinAdmin)
