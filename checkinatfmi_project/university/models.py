from django.db import models

import checkinatfmi.translations_bg as translate


class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length=255, verbose_name = translate.name)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = translate.specialty
        verbose_name_plural = translate.specialties

class PlaceManager(models.Manager):
    pass

class Place(models.Model):
    """
    Represents physical place at the university/institution
    Fields:
        name - The ID of the room (e.g. number or name)
        capacity - the physical capacity of the room (used to indicate
                   the current load of the room)
    Methods:
        unicode - print representation
    """
    name = models.CharField(max_length=255, verbose_name = translate.name)
    capacity = models.IntegerField(verbose_name = translate.capacity)
    objects = models.Manager()
    places = PlaceManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = translate.place
        verbose_name_plural = translate.places
