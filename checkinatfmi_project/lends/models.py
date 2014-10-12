from datetime import datetime

from django.db import models

from identifications.models import Book
from identifications.models import Cardowner


class LendRequest(models.Model):
    WAITING = 'W'
    LEND = 'L'
    RETURNED = 'R'
    DELAYED = 'D'
    CANCELED = 'C'

    REQUEST_STATUSES = (
        (WAITING, 'WAITING'),
        (LEND, 'LEND'),
        (RETURNED, 'RETURNED'),
        (DELAYED, 'DELAYED'),
        (CANCELED, 'CANCELED'),
    )

    date = models.DateTimeField(default=datetime.now)
    book = models.ForeignKey('identifications.Book')
    requester = models.ForeignKey('identifications.Cardowner')

    status = models.CharField(choices=REQUEST_STATUSES, max_length=2, default=WAITING)

    def __unicode__(self):
        return u"%s -> %s" % (self.requester, self.book)
