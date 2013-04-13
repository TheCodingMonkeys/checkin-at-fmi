from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 63)
    card_key = models.CharField(max_length = 63)

    def __unicode__(self):
        return self.name

    @staticmethod
    def create(key):
        user = User()
        user.name = key
        user.card_key = key
        user.save()
        return user
