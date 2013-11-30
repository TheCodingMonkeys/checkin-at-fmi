
from django import forms
from django.contrib import admin

from genericadmin.admin import GenericAdminModelAdmin
from relatedwidget import RelatedWidgetWrapperBase

from models import Activity, Borrow, Checkin, Carrier

class CarrierForm(forms.ModelForm):
    state = forms.ChoiceField(choices=Carrier.CARRIER_STATES, widget=forms.Select)
    class Meta:
        model = Carrier


class ActivityAdmin(RelatedWidgetWrapperBase, admin.ModelAdmin):
    pass

class CarrierAdmin(GenericAdminModelAdmin):
    content_type_whitelist = (
        'identifications/book',
        'identifications/cardowner',
    )
    readonly_fields = ('data',)
    form = CarrierForm


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Borrow)
admin.site.register(Checkin)
admin.site.register(Carrier, CarrierAdmin)
