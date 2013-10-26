from django.contrib import admin

from models import User, Student, Specialty

class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'card_key']
    list_display = ['first_name', 'last_name']


class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'card_key', 'specialty']
    

class SpecialtyAdmin(admin.ModelAdmin):
	fields = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Specialty, SpecialtyAdmin)