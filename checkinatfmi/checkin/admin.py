from django.contrib import admin

from models import Checkin

class CheckinAdmin(admin.ModelAdmin):
    fields = ['user', 'place', 'time', 'active']
    list_display = ['user', 'place', 'time', 'active']

admin.site.register(Checkin, CheckinAdmin)
