import datetime
import random

import kronos

from models import Activity, Checkin


@kronos.register('59 21 * * *')
def auto_checkout():
    active_checkins = Checkin.checkins.active()
    for checkin in active_checkins:
        auto_checkout_activity = Activity()
        auto_checkout_activity = checkin.checkin_activity
        auto_checkout_activity.time = datetime.datetime.now()
	auto_checkout_activity.id = None
        auto_checkout_activity.save()
        checkin.checkout_activity = auto_checkout_activity
        checkin.save()
