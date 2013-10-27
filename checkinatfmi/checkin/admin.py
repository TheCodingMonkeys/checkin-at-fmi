import datetime

from django.contrib import admin

from django import forms

from models import Checkin, Bookrent
from places.models import Place

class CheckinAdmin(admin.ModelAdmin):
    fields = ['user', 'place', 'checkin_time', 'checkout_time', 'active']
    list_display = ['user', 'place', 'checkin_time', 'checkout_time', 'active']

admin.site.register(Checkin, CheckinAdmin)



class BookrentAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookrentAdminForm, self).__init__(*args, **kwargs)
        self.fields['checkin'].queryset = Checkin.objects.filter(place=self.instance.place, active=True)


class BookrentAdmin(admin.ModelAdmin):
    fields = ['checkin', 'book','place', 'checkin_time', 'checkout_time', 'rented']
    list_display = ['checkin', 'book', 'rented']

    form = BookrentAdminForm
    #limit_choices_to = {'checkin__place' : '' }
    #limit_choices_to = {'checkin___active': True }

admin.site.register(Bookrent, BookrentAdmin)