import copy
import datetime

from django import forms
from django.contrib import admin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from genericadmin.admin import GenericAdminModelAdmin
from relatedwidget import RelatedWidgetWrapperBase
from salmonella.admin import SalmonellaMixin

from django_extensions.admin import ForeignKeyAutocompleteAdmin

from models import Activity, Borrow, Checkin, Carrier


class ActivityAdmin(RelatedWidgetWrapperBase, SalmonellaMixin, admin.ModelAdmin):
    # create an ajax form class using the factory function
    #                     model,fieldlist,   [form superclass]
    # form = make_ajax_form(Activity, {'carrier':'identification'})
    salmonella_fields = ('carrier',)
    search_fields = ('carrier__cardowner__faculty_number',)



class BorrowAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('borrower', 'borrow', 'handback')
    #related_search_fields = {
        #'borrower': ('faculty_number',),
        #'borrow': ('carrier__data',),
        #'handback': ('carrier__data',),
    #}

    #fields = ('borrower', 'borrow', 'handback')

    #class Media:
        #js = ("//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",)


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
    list_display = ('cardowner', 'checkin_time_admin', 'checkout_time_admin', 'place', 'is_active', )
    list_filter = ('checkin_activity__client__place',)
    search_fields = ['checkin_activity__carrier__cardowner__faculty_number']


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Carrier, CarrierAdmin)
admin.site.register(Checkin, CheckinAdmin)
