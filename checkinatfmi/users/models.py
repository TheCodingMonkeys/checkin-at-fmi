from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length = 63, default='')
    last_name = models.CharField(max_length = 63, default='')

    card_key = models.CharField(max_length = 63)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def create(key):
        user = User()
        user.first_name = "Unregistered"
        user.card_key = key
        user.save()
        return user

class Student(User):
    """
    Model for Students in university
    """
    specialty = models.ForeignKey('Specialty')


class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length = 63, default='')    

    def __unicode__(self):
        return self.name