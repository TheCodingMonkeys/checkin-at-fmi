from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

from managers import CheckinManager

class Activity(models.Model):
    time = models.DateTimeField()
    client = models.ForeignKey('clients.Client')
    carrier = models.ForeignKey('Carrier', verbose_name='Indentification Carrier')

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
        verbose_name_plural = 'activities'


class Carrier(models.Model):
    UNREGISTERED = 'U'
    REGISTERED = 'R'
    BANNED = 'B'
    CARRIER_STATES = (
        (UNREGISTERED, 'UNREGISTERED'),
        (BANNED, 'BANNED'),
        (REGISTERED, 'REGISTERED'),
    )
    
    state = models.CharField(choices=CARRIER_STATES, max_length=2, default=UNREGISTERED)

    data = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    identification = generic.GenericForeignKey('content_type', 'object_id')

    def is_registered(self):
        return self.state == Carrier.REGISTERED 

    def __unicode__(self):
        return u'%s %s: %s' % (self.state, self.content_type, self.identification)

    class Meta:
        verbose_name = "Identification Carrier"


class Borrow(models.Model):
    borrower = models.ForeignKey('identifications.Cardowner')
    borrow = models.ForeignKey(Activity, related_name='borrowes')
    handback = models.ForeignKey(Activity, related_name='handbackes')

    @property
    def borrowed_item(self):
        return self.borrow.carrier.identification

    def __unicode__(self):
        return u'%s -> %s' % (borrower, borrowed_item)


class Checkin(models.Model):
    checkin_activity = models.ForeignKey(Activity, related_name='checkins')
    checkout_activity = models.ForeignKey(Activity, related_name='checkouts', null=True)

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
