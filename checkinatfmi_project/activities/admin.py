import copy
import datetime

from django import forms
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin
from relatedwidget import RelatedWidgetWrapperBase

from models import Activity, Borrow, Checkin, Carrier


class ActivityAdmin(RelatedWidgetWrapperBase, admin.ModelAdmin):
    pass


class CarrierForm(forms.ModelForm):
    state = forms.ChoiceField(choices=Carrier.CARRIER_STATES, widget=forms.Select)
    #list_display = ('fistname')

    class Meta:
        model = Carrier


class CarrierAdmin(GenericAdminModelAdmin):
    content_type_whitelist = (
        'identifications/book',
        'identifications/cardowner',
    )
    readonly_fields = ('data',)
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
    list_display = ('cardowner', 'checkin_time', 'checkout_time', 'place', 'is_active', ) 
    list_filter = ('checkin_activity__client__place',)
    search_fields = ['checkin_activity__carrier__cardowner__faculty_number']


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Borrow)
admin.site.register(Checkin, CheckinAdmin)
admin.site.register(Carrier, CarrierAdmin)
