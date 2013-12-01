from django.contrib import admin

from models import Specialty
from models import Place


class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'capacity']
    list_display = ['name', 'capacity']


class SpecialtyAdmin(admin.ModelAdmin):
	fields = ['name']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
