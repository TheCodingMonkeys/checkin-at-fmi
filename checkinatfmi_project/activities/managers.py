from django.db import models

class CheckinManager(models.Manager):
    def active(self):
        return super(CheckinManager, self).get_query_set()\
                .filter(checkout_activity__isnull=True)

    def filter_by_place_and_month(self, place, month):
        return super(CheckinManager, self).get_query_set()\
                .filter(
                    checkin_activity__client__place=place,
                    checkin_activity__time__month=month
                )

    def filter_by_place_day_and_month(self, place, day, month):
        return super(CheckinManager, self).get_query_set()\
                .filter(
                        checkin_activity__client__place=place,
                        checkin_activity__time__month=month,
                        checkin_activity__time__day=day
                )

    def filter_by_place_and_specialty(self, place, specialty):
        return super(CheckinManager, self).get_query_set()\
                .filter(
                    checkin_activity__client__place=place,
                    checkin_activity__carrier__cardowner__specialty=specialty
                )

    def filter_by_place_and_grade(self, place, grade):
        return super(CheckinManager, self).get_query_set()\
                .filter(
                    checkin_activity__client__place=place,
                    checkin_activity__carrier__cardowner__grade=grade
                )
