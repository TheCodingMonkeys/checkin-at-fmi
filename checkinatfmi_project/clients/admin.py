from django.contrib import admin

import checkinatfmi.translations_bg as translate

from models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = ['mac', 'status', 'status_changed', 'place']
    readonly_fields = ['status_changed', 'mac']
    list_display = ['mac', 'place', 'status_changed', 'status']


class ProxyClient(Client):
    class Meta:
        proxy = True
        app_label = 'university'
        verbose_name = translate.client
        verbose_name_plural = translate.clients


admin.site.register(ProxyClient, ClientAdmin)
