from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models


class Identification(models.Model):
    """
    
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u'%s: %s' % (self.content_type, self.content_object)


class Cardowner(models.Model):
    """
    Basic model of person with a card
    """
    identification = generic.GenericRelation(Identification)
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
    identification = generic.GenericRelation(Identification)
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
