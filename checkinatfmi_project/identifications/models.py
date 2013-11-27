from django.contrib.contenttypes import generic
from django.db import models


class Cardowner(models.Model):
    """
    Basic model of person with a card
    """
    carrier = generic.GenericRelation('activities.Carrier')
    faculty_number = models.IntegerField()
    grade = models.IntegerField()
    specialty = models.ForeignKey('Specialty')
    susi_name = models.CharField(max_length=63, null=True, blank=True)
    sudi_password = models.CharField(max_length=63, null=True, blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.faculty_number, self.specialty)


class Book(models.Model):
    """
    Book in library
    """
    carrier = generic.GenericRelation('activities.Carrier')
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=63)

    def __unicode__(self):
        return u"%s: %s" % (self.title, self.isbn)


class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name
