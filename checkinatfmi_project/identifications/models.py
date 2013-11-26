from django.db import models


class Identification(models.Model):
    nature = models.IntegerField()


class Cardowner(models.Model):
    identificartion = models.OneToOneField(Identification)

    faculty_number = models.IntegerField()
    grade = models.IntegerField()
    specialty = models.ForeignKey('Specialty')
    susi_name = models.CharField(max_length=63, null=True, blank=True)
    sudi_password = models.CharField(max_length=63, null=True, blank=True)


class Book(models.Model):
    identificartion = models.OneToOneField(Identification)

    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=63)


class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return self.name


