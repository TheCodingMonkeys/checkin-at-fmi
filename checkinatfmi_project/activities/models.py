from datetime import datetime, timedelta

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

import checkinatfmi.translations_bg as translate

from managers import BorrowManager
from managers import CheckinManager


DEFAULT_BORROW_DAYS = 7 # Extract in settings

class Activity(models.Model):
    time = models.DateTimeField(verbose_name=translate.time)
    client = models.ForeignKey('clients.Client', verbose_name = translate.client)
    carrier = models.ForeignKey('Carrier',
                verbose_name=translate.carrier)

    @property
    def place(self):
        return self.client.place

    @classmethod
    def create(cls, time, client, carrier):
        activity = cls(time=time, client=client, carrier=carrier)
        activity.save()
        carrier.identification.register_activity(activity)
        return activity

    def __unicode__(self):
        return u'%s: %s > %s' % (
            self.time,
            self.carrier.identification,
            self.place
        )

    class Meta:
        verbose_name = translate.activity
        verbose_name_plural = translate.activities


class Carrier(models.Model):
    UNREGISTERED = 'U'
    REGISTERED = 'R'
    BANNED = 'B'
    CARRIER_STATES = (
        (UNREGISTERED,  translate.unregistered),
        (BANNED, translate.banned),
        (REGISTERED, translate.registered),
    )

    state = models.CharField(verbose_name = translate.state,
                choices=CARRIER_STATES,
                max_length=2,
                default=UNREGISTERED
            )

    data = models.CharField(verbose_name = translate.data, max_length=255, unique=True)
    content_type = models.ForeignKey(ContentType, verbose_name = translate.content_type, null=True)
    object_id = models.PositiveIntegerField(verbose_name = translate.object_id, null=True)
    identification = generic.GenericForeignKey('content_type', 'object_id')

    def is_registered(self):
        return self.state == Carrier.REGISTERED

    def __unicode__(self):
        return u'%s %s: %s' % (self.state, self.content_type, self.identification)

    class Meta:
        verbose_name = translate.carrier
        verbose_name_plural = translate.carriers


class Borrow(models.Model):
    borrower = models.ForeignKey('identifications.Cardowner', verbose_name = translate.borrower)
    borrow = models.ForeignKey(Activity, verbose_name = translate.borrow_activity, related_name='borrowes')
    handback = models.ForeignKey(Activity, verbose_name = translate.handback_activity, related_name='handbackes', blank=True, null=True)
    days = models.PositiveSmallIntegerField(verbose_name = translate.borrow_days, default=DEFAULT_BORROW_DAYS)

    objects = models.Manager()
    borrows = BorrowManager()

    @property
    def borrowed_item(self):
        return self.borrow.carrier.identification

    @property
    def return_time(self):
        return self.borrow.time + timedelta(self.days)

    def __unicode__(self):
        return u'%s -> %s' % (self.borrower, self.borrowed_item)

    class Meta:
        verbose_name = translate.borrow
        verbose_name_plural = translate.borrows


class Checkin(models.Model):
    checkin_activity = models.ForeignKey(Activity,
            verbose_name = translate.checkin_activity,
            related_name='checkins')
    checkout_activity = models.ForeignKey(Activity,
            verbose_name = translate.checkout_activity,
            related_name='checkouts',
            null=True)

    objects = models.Manager()
    checkins = CheckinManager()

    @property
    def cardowner(self):
        return self.checkin_activity.carrier.identification

    @property
    def place(self):
        return self.checkin_activity.client.place

    @property
    def checkin_time(self):
        return self.checkin_activity.time

    def checkin_time_admin(self):
        return self.checkin_activity.time

    checkin_time_admin.admin_order_field = 'checkin_activity__time'

    @property
    def checkout_time(self):
        if self.checkout_activity:
            return self.checkout_activity.time
        else:
            return None

    def checkout_time_admin(self):
        if self.checkout_activity:
            return self.checkout_activity.time
        else:
            return None

    checkout_time_admin.admin_order_field = 'checkout_activity__time'

    @property
    def cardowner(self):
        return self.checkin_activity.carrier.identification

    def is_active(self):
        return not self.checkout_activity

    def active_time(self):
        checkin_end_time = datetime.now()\
                            if self.checkout_activity is None\
                            else self.checkout_activity.time
        return checkin_end_time - self.checkin_activity.time

    def __unicode__(self):
        return u'%s @ %s' % (self.cardowner, self.checkin_activity)

    class Meta:
        verbose_name = translate.checkin
        verbose_name_plural = translate.checkins
