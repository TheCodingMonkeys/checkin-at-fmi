from django.db import models


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
    name = models.CharField(max_length=15, null=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name
