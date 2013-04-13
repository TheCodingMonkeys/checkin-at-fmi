from django.db import models

from users.models import User
from places.models import Place

class Checkin (models.Model):
    user = models.ForeignKey(User)
    place = models.ForeignKey(Place)
    time = models.DateTimeField()

    def __unicode__(self):
        return "%s -> %s at: %s" % (self.user, self.place, self.time)

    @staticmethod
    def checkin (user, place, time):
        print "Saving.."
        checkin = Checkin()
        checkin.user = user
        checkin.place = place
        checkin.time = time
        
        checkin.save()
        print "Saved"
