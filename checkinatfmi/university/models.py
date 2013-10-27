from django.db import models

from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    """
    User with app settings.
    """
    card_key = models.CharField(max_length = 63, unique=True, blank=True, null=True)
    specialty = models.ForeignKey('Specialty', blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    valid = models.BooleanField(default = False)

    objects = UserManager()

    @classmethod
    def create(cls, key = ''):
        user = cls()
        user.username = cls.objects.count()
        user.first_name = 'Unregistered'
        user.card_key = key
        user.password = 'password'
        user.save()
        return user

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Cardowner'           

class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length = 63, default='')    

    def __unicode__(self):
        return self.name


class Book(models.Model):
    """
    Book in University
    """
    title = models.CharField(max_length = 255)
    book_id = models.CharField(max_length = 63)

    def __unicode__(self):
        return self.title