from django.contrib import admin

from models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'card_key']
    # list_display = ['name']

admin.site.register(User, UserAdmin)
