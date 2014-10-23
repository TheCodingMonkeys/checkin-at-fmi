from django.conf import settings
from django.contrib.contenttypes import generic
from django.db import models

from django_resized import ResizedImageField

import checkinatfmi.translations_bg as translate

from activities.models import Borrow
from activities.models import Checkin


class Cardowner(models.Model):
    """
    Basic model of person with a card
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True)

    carrier = generic.GenericRelation('activities.Carrier', verbose_name = translate.carrier)
    faculty_number = models.IntegerField(unique=True, verbose_name = translate.faculty_number)
    grade = models.IntegerField(verbose_name = translate.grade)
    specialty = models.ForeignKey('university.Specialty', verbose_name = translate.specialty)
    susi_name = models.CharField(max_length=63, null=True, blank=True, verbose_name = translate.susi_name)
    sudi_password = models.CharField(max_length=63, null=True, blank=True, verbose_name = translate.sudi_password)

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

    class Meta:
        verbose_name = translate.cardowner
        verbose_name_plural = translate.cardowners


class Book(models.Model):
    """
    Book in library
    """
    carrier = generic.GenericRelation('activities.Carrier', verbose_name = translate.carrier)
    category = models.ForeignKey('BookCategory', verbose_name = translate.category)
    title = models.CharField(max_length=255, verbose_name = translate.title)
    author = models.CharField(max_length=255, verbose_name = translate.author, blank=True)
    publisher = models.CharField(max_length=255, verbose_name = translate.publisher, blank=True)
    year = models.PositiveSmallIntegerField(blank=True, verbose_name = translate.year)
    isbn = models.CharField(max_length=63, verbose_name = translate.isbn)
    copies = models.PositiveSmallIntegerField(default=1, verbose_name = translate.copies)

    cover = ResizedImageField(
        upload_to='covers',
        max_width=400,
        blank=True,
        verbose_name = translate.cover,
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

    def is_available(self):
        if self.available_count > 0:
            return True
        return False

    class Meta:
        verbose_name = translate.book
        verbose_name_plural = translate.books


class BookCategory(models.Model):
    title = models.CharField(max_length=80, verbose_name = translate.title)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = translate.category
        verbose_name_plural = translate.categories
