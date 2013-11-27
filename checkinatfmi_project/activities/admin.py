from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin

from models import Activity, Borrow, Checkin, Carrier


class CarrierAdmin(GenericAdminModelAdmin):
    content_type_whitelist = ('identifications/book',
            'identifications/cardowner')


admin.site.register(Activity)
admin.site.register(Borrow)
admin.site.register(Checkin)
admin.site.register(Carrier, CarrierAdmin)
