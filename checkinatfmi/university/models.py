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
    specialty = models.ForeignKey('Specialty', blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)

    objects = UserManager()

    @classmethod
    def create(cls, key = ''):
        user = cls()
        user.username = cls.objects.count()
        user.first_name = 'Unregistered'
        user.card_key = key

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