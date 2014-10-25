import copy
import datetime

from django import forms
from django.contrib import admin

import autocomplete_light
from genericadmin.admin import GenericAdminModelAdmin
from salmonella.admin import SalmonellaMixin

from checkinatfmi import mailer

from identifications.models import Cardowner
from lends.models import LendRequest
from models import Activity, Borrow, Checkin, Carrier

import checkinatfmi.translations_bg as translate

class ActivityAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('carrier',)


class BorrowAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('borrow', 'handback')
    form = autocomplete_light.modelform_factory(Borrow)
    list_display = ('borrower', 'borrowed_item', 'give_back_time', '_time_left')
    search_fields = (
        'borrower__faculty_number',
        'borrower__user__first_name',
        'borrower__user__last_name',
    )

    def save_model(self, request, obj, form, change):
        if obj.handback and 'handback' in form.changed_data:
            book_requests = LendRequest.objects.filter(book=obj.borrowed_item, status=LendRequest.WAITING).order_by('date')
            if len(book_requests) > 0:
                lend_request = book_requests[0]
                lend_request.status = LendRequest.FOR_LEND
                mailer.send_borrow_invite(lend_request.requester, obj.borrowed_item)
                lend_request.save()

        obj.save()


class CarrierForm(forms.ModelForm):
    state = forms.ChoiceField(choices=Carrier.CARRIER_STATES, widget=forms.Select, label = translate.state)

    class Meta:
        model = Carrier


class CarrierAdmin(GenericAdminModelAdmin):
    content_type_whitelist = (
        'identifications/book',
        'identifications/cardowner',
    )
    search_fields = ['book__title',
        'book__isbn',
        'cardowner__faculty_number',
        'cardowner__user__first_name',
        'cardowner__user__last_name',
        'data'
    ]

    list_filter = ('content_type', 'state')
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
