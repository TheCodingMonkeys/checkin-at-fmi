from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models


class ActivityManager(models.Manager):
    def add_activity(self, time, client, carrier):
        pass


class Activity(models.Model):
    time = models.DateTimeField()
    client = models.ForeignKey('clients.Client')
    carrier = models.ForeignKey('Carrier', verbose_name='Indentification Carrier')

    activities = ActivityManager()

    @classmethod
    def create(cls, time, client, carrier):
        activity = cls(time=time, client=client, carrier=carrier)
        activity.save()
        carrier.identification.register_activity(activity)
        return activity

    def __unicode__(self):
        return u'%s: %s at %s' % (self.time, self.client, self.carrier)

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
        return u'%s: %s' % (self.state, self.content_type)

    class Meta:
        verbose_name = "Identification Carrier"


class Borrow(models.Model):
    borrower = models.ForeignKey('identifications.Cardowner')
    borrow = models.ForeignKey(Activity, related_name='borrowes')
    handback = models.ForeignKey(Activity, related_name='handbackes')

    def register_activity(self, activity):
        print 'hello'

    def _get_borrowed_item(self):
        return self.borrow.carrier.identification

    borrowed_item = property(_get_borrowed_item)

    def __unicode__(self):
        return '%s -> %s' % (borrower, borrowed_item)


class Checkin(models.Model):
    checkin_activity = models.ForeignKey(Activity, related_name='checkins')
    checkout_activity = models.ForeignKey(Activity, related_name='checkouts', null=True)

    def _get_cardowner(self):
        return self.checkin_activity.carrier.identification

    cardowner = property(_get_cardowner)

    def __unicode__(self):
        return '%s @ %s' % (self.cardowner, self.checkin_activity)
