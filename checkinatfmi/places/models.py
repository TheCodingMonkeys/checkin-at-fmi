from django.db import models

class Place(models.Model):
    name = models.CharField(max_length = 15, null = True)
    capacity = models.IntegerField(null = True, blank = True)

    def __unicode__(self):
        return self.name
