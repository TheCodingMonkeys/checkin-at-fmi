from django.contrib import admin

from models import Specialty, CustomUser

#class UserAdmin(admin.ModelAdmin):
#    fields = ['first_name', 'last_name', 'card_key']
#    list_display = ['first_name', 'last_name']

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'card_key', 'groups', 'specialty', 'grade']
    list_display = ['first_name', 'last_name', 'specialty']
    

class SpecialtyAdmin(admin.ModelAdmin):
	fields = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Specialty, SpecialtyAdmin)