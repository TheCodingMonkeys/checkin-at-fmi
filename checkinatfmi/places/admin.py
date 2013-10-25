from django.contrib import admin

from models import Place

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'capacity']
    list_display = ['name', 'capacity']

admin.site.register(Place, PlaceAdmin)
