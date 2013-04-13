from django.db import models

class Place(models.Model):
    mac = models.CharField(max_length = 63)
    name = models.CharField(max_length = 15, null = True)
