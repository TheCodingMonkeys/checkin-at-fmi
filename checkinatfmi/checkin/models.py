from django.db import models

from users.models import User
from places.models import Place

class Checkin (models.Model):
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)
    time = models.DateTimeField()
    active = models.BooleanField(default = False)

    def __unicode__(self):
        return "%s -> %s at: %s" % (self.user, self.place, self.time)

    @staticmethod
    def checkin (user, place, time):
        checkin = Checkin()
        checkin.user = user
        checkin.place = place
        checkin.time = time
        checkin.active = True
        checkin.save()

    def checkout(self):
        self.active = False
        self.save()
