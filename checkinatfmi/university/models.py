from django.db import models


# Sudents
# Teachers
# Admin

from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    """
    User with app settings.
    """
    card_key = models.CharField(max_length = 63, blank=True, null=True)

    objects = UserManager()

    @classmethod
    def create(cls, key = ''):
        user = cls(key=title)
        user.card_key = key

        return user

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Student(CustomUser):
    """
    Model for Students in university
    """
    specialty = models.ForeignKey('Specialty')

    class Meta:
        verbose_name = 'Student'           


class Specialty(models.Model):
    """
    Specialty in University
    """
    name = models.CharField(max_length = 63, default='')    

    def __unicode__(self):
        return self.name