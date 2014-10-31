"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Place


class SimpleTest(TestCase):
    def test_simple_place_creation(self):
        """
        Creates test place
        """
        places = Place.objects.filter(name="Test Place")
        [place.delete() for place in places]

        place = Place()
        place.name = "Test Place"
        place.capacity = 20
        place.save()

        place = Place.objects.filter(name="Test Place")
        print place
        self.assertNotEqual(place, None)
