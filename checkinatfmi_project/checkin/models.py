from django.db import models

from university.models import CustomUser, Book
from places.models import Place

from datetime import datetime

class Checkin (models.Model):
    user = models.ForeignKey(CustomUser)
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


class Bookrent (models.Model):
    #user = models.ForeignKey(CustomUser, null = True)
    book = models.ForeignKey(Book)
    place = models.ForeignKey(Place)
    checkin = models.ForeignKey(Checkin, null = True)
    checkin_time = models.DateTimeField(null = True)
    checkout_time = models.DateTimeField(null = True, blank = True)
    rented = models.BooleanField(default = False)

    def __unicode__(self):
        if self.checkin and self.checkin.user:
            return "%s -> %s at: %s" % (self.checkin.user, self.book, self.checkin_time)
        else:
            return "%s picked at: %s" % (self.book, self.checkin_time)
     
    @staticmethod
    def bookrent (place, book, time):
        rent = Bookrent()
        rent.book = book
        rent.place = place
        rent.checkin_time = time
        rent.rented = True
        rent.save()
        return rent

    def bookreturn(self, checkout_time):
        self.rented = False
        self.checkout_time = checkout_time
        self.save()

