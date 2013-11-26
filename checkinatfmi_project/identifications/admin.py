
from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin

from models import Identification, Cardowner, Book, Specialty


class IdentificationAdmin(GenericAdminModelAdmin):
    content_type_whitelist = ('identifications/book',
            'identifications/cardowner')


admin.site.register(Identification, IdentificationAdmin)
admin.site.register(Cardowner)
admin.site.register(Book)
admin.site.register(Specialty)

