from django.contrib import admin

from models import Checkin

class CheckinAdmin(admin.ModelAdmin):
    fields = ['user', 'place', 'time']
    list_display = ['user', 'place', 'time']

admin.site.register(Checkin, CheckinAdmin)
