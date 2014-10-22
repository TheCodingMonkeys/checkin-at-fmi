from django.db import models

import checkinatfmi.translations_bg as translate

from university.models import Place

class Client(models.Model):
    mac = models.CharField(max_length=63, verbose_name=translate.client_mac)
    status = models.BooleanField(verbose_name=translate.state)
    status_changed = models.DateTimeField(auto_now=True, verbose_name = translate.updated_time)
    place = models.ForeignKey(Place, null=True, verbose_name = translate.place)

    def __unicode__(self):
        return u"%s @ %s" % (self.mac, self.place)

    class Meta:
        verbose_name = translate.client
        verbose_name_plural = translate.clients
