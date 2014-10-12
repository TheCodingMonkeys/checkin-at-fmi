from django.contrib import admin

from models import LendRequest


class LendRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(LendRequest, LendRequestAdmin)
