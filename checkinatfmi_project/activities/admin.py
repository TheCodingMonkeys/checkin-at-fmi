from django.contrib import admin

from models import Activity, Borrow, Checkin, Carrier
from identifications.models import Identification


admin.site.register(Activity)
admin.site.register(Borrow)
admin.site.register(Checkin)
admin.site.register(Carrier)
