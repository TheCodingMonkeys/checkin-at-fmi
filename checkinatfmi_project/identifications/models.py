from django.conf import settings
from django.contrib.contenttypes import generic
from django.db import models

from activities.models import Borrow
from activities.models import Checkin

from django_resized import ResizedImageField

class Cardowner(models.Model):
    """
    Basic model of person with a card
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True)

    carrier = generic.GenericRelation('activities.Carrier')
    faculty_number = models.IntegerField(unique=True)
    grade = models.IntegerField()
    specialty = models.ForeignKey('university.Specialty')
    susi_name = models.CharField(max_length=63, null=True, blank=True)
    sudi_password = models.CharField(max_length=63, null=True, blank=True)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @classmethod
    def register_activity(self, activity):
        is_checkin = True
        active_checkins = Checkin.checkins.active()
        for checkin in active_checkins:
            if checkin.checkin_activity.place == activity.place and \
                checkin.cardowner == activity.carrier.identification:
                is_checkin = False
                checkin.checkout_activity = activity
                checkin.save()

        if is_checkin:
            checkin = Checkin()
            checkin.checkin_activity = activity
            checkin.save()

    def __unicode__(self):
        return u'%s (%s): %s' % (self.first_name, self.faculty_number, self.specialty)


class Book(models.Model):
    """
    Book in library
    """
    carrier = generic.GenericRelation('activities.Carrier')
    category = models.ForeignKey('BookCategory')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    year = models.PositiveSmallIntegerField(blank=True)
    isbn = models.CharField(max_length=63)
    copies = models.PositiveSmallIntegerField(default=1)

    cover = ResizedImageField(
        upload_to='covers',
        max_width=400,
        blank=True,
    )

    def __unicode__(self):
        return u'%s: %s' % (self.title, self.isbn)

    @classmethod
    def register_activity(self, activity):
        is_borrow = True
        active_borrows = Borrow.borrows.active()
        for borrow in active_borrows:
            if borrow.borrow.place == activity.place and \
                borrow.borrower == activity.carrier.identification:
                is_borrow = False
                borrow.handback = activity
                borrow.save()

        if is_borrow:
            borrow = Borrow()
            borrow.borrow = activity
            borrow.save()

    # TODO: Implement this!
    def available_count(self):
        return 1

class BookCategory(models.Model):
    title = models.CharField(max_length=80)

    def __unicode__(self):
        return unicode(self.title)
