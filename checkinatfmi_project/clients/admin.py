from django.contrib import admin

from models import Client

class ClientAdmin(admin.ModelAdmin):
    fields = ['mac', 'status', 'status_changed', 'place']
    readonly_fields = ['status_changed', 'mac']
    list_display = ['mac', 'status_changed', 'status']

class ProxyClient(Client):
    class Meta:
        proxy = True
        app_label = 'university'
        verbose_name = 'Checkin client'
        verbose_name_plural = 'Checkin clients'

admin.site.register(ProxyClient, ClientAdmin)
