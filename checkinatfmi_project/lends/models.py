from datetime import datetime

from django.db import models

import checkinatfmi.translations_bg as translate

from identifications.models import Book
from identifications.models import Cardowner


class LendRequest(models.Model):
    WAITING = 'W'
    FOR_LEND = 'L'
    RETURNED = 'R'
    DELAYED = 'D'
    CANCELED = 'C'

    REQUEST_STATUSES = (
        (WAITING, translate.waiting),
        (FOR_LEND, translate.for_lend),
        (RETURNED, translate.returned),
        (DELAYED, translate.delayed),
        (CANCELED, translate.canceled),
    )

    date = models.DateTimeField(default=datetime.now, verbose_name = translate.date)
    book = models.ForeignKey('identifications.Book', verbose_name = translate.book)
    requester = models.ForeignKey('identifications.Cardowner', verbose_name = translate.requester)

    status = models.CharField(choices=REQUEST_STATUSES, max_length=2, default=WAITING, verbose_name = translate.state)

    def __unicode__(self):
        return u"%s -> %s" % (self.requester, self.book)

    class Meta:
        verbose_name = translate.lend_request
        verbose_name_plural = translate.lend_requests
