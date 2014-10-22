from django.contrib import admin

import checkinatfmi.translations_bg as translate

from models import LendRequest


class LendRequestAdmin(admin.ModelAdmin):
    pass

class LendRequestProxy(LendRequest):
    class Meta:
        proxy = True
        app_label = 'activities'
        verbose_name = translate.lend_request
        verbose_name_plural = translate.lend_requests

admin.site.register(LendRequestProxy, LendRequestAdmin)

