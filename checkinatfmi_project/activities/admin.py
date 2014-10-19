import copy
import datetime

from django import forms
from django.contrib import admin

import autocomplete_light
from genericadmin.admin import GenericAdminModelAdmin
from salmonella.admin import SalmonellaMixin

from models import Activity, Borrow, Checkin, Carrier
from identifications.models import Cardowner


class ActivityAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('carrier',)


class BorrowAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('borrow', 'handback')
    form = autocomplete_light.modelform_factory(Borrow)


class CarrierForm(forms.ModelForm):
    state = forms.ChoiceField(choices=Carrier.CARRIER_STATES, widget=forms.Select)

    class Meta:
        model = Carrier


class CarrierAdmin(GenericAdminModelAdmin):
    content_type_whitelist = (
        'identifications/book',
        'identifications/cardowner',
    )
    readonly_fields = ('data',)
    search_fields = ['book__title', 'cardowner__faculty_number', 'data']
    form = CarrierForm


def checkout(modeladmin, request, queryset):
    for checkin in queryset:
        activity = Activity()
        activity.time = datetime.datetime.now()
        activity.carrier = checkin.checkin_activity.carrier
        activity.client = checkin.checkin_activity.client
        activity.save()
        checkin.checkout_activity = activity
        checkin.save()


class CheckinAdmin(admin.ModelAdmin):
    actions = [checkout]
    list_display = ('cardowner', 'checkin_time_admin', 'checkout_time_admin', 'place', 'is_active', )
    list_filter = ('checkin_activity__client__place',)
    search_fields = ['checkin_activity__carrier__cardowner__faculty_number']


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Checkin, CheckinAdmin)
