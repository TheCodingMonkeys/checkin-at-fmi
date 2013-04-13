from django.contrib import admin

from models import Place

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'mac']
    list_display = ['name', 'mac']

admin.site.register(Place, PlaceAdmin)
