from models import Client

from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    fields = ['mac', 'status']
    list_display = ['mac', 'status']

admin.site.register(Client, ClientAdmin)
