from django.contrib import admin

from models import Client

class ClientAdmin(admin.ModelAdmin):
    fields = ['mac', 'status', 'status_changed', 'place']
    readonly_fields = ['status_changed',]
    list_display = ['mac', 'status']

admin.site.register(Client, ClientAdmin)
