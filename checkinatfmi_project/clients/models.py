from django.db import models

from university.models import Place

class Client(models.Model):
    mac = models.CharField(max_length=63)
    status = models.BooleanField()
    status_changed = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(Place, null=True)

    def __unicode__(self):
        return u"%s @ %s" % (self.mac, self.place)
