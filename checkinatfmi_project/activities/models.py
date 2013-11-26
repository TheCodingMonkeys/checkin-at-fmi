from django.db import models


class Activity(models.Model):
    time = models.DateTimeField()
    client = models.ForeignKey('clients.Client')
    carrier = models.ForeignKey('Carrier', verbose_name='Indentification Carrier')

    def __unicode__(self):
        return u'%s: %s at %s' % (self.time, self.client, self.carrier)

    class Meta:
        verbose_name_plural = 'activities'


class Carrier(models.Model):
    state = models.IntegerField()
    data = models.CharField(max_length=127)
    medium = models.IntegerField()
    identification = models.ForeignKey('identifications.Identification')

    def __unicode__(self):
        return u'%s (%s): %s' % (self.state, self.medium, self.identification)


class Borrow(models.Model):
    borrow = models.ForeignKey(Activity, related_name='borrowes')
    handback = models.ForeignKey(Activity, related_name='handbackes')
    borrower = models.ForeignKey('identifications.Cardowner')

    def _get_borrowed_item(self):
        return self.borrow.carrier.identification

    borrowed_item = property(_get_borrowed_item)

    def __unicode__(self):
        return '%s -> %s' % (borrower, borrowed_item)


class Checkin(models.Model):
    checkin_activity = models.ForeignKey(Activity, related_name='checkins')
    checkout_activity = models.ForeignKey(Activity, related_name='checkouts')

    def _get_cardowner(self):
        return self.checkin_activity.carrier.identification

    cardowner = property(_get_cardowner)

    def __unicode__(self):
        return '%s' % (cardowner)
