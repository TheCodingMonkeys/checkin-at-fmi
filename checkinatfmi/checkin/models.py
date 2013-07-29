from django.db import models

from users.models import User
from places.models import Place

from datetime import datetime

class Checkin (models.Model):
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)
    checkin_time = models.DateTimeField(null = True)
    checkout_time = models.DateTimeField(null = True, blank = True)
    active = models.BooleanField(default = False)

    def __unicode__(self):
        return "%s -> %s at: %s" % (self.user, self.place, self.checkin_time)

    @staticmethod
    def checkin (user, place, time):
        checkin = Checkin()
        checkin.user = user
        checkin.place = place
        checkin.checkin_time = time
        checkin.active = True
        checkin.save()
        return checkin

    def checkout(self, checkout_time):
        self.active = False
        self.checkout_time = checkout_time
        self.save()
