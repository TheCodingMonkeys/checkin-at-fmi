from django.contrib import admin

import checkinatfmi.translations_bg as translate

from models import LendRequest


class LendRequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'book', 'date', 'status',)
    search_fields = (
        'requester__faculty_number',
        'requester__user__first_name',
        'requester__user__last_name',
    )


class LendRequestProxy(LendRequest):
    class Meta:
        proxy = True
        app_label = 'activities'
        verbose_name = translate.lend_request
        verbose_name_plural = translate.lend_requests


admin.site.register(LendRequestProxy, LendRequestAdmin)

