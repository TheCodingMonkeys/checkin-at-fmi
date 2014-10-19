import datetime
import random

import kronos

from checkinatfmi import mailer

from models import Activity, Checkin, Borrow


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

@kronos.register('59 21 * * *')
def auto_remind():
    active_borrows = Borrow.borrows.active()
    for borrow in active_borrows:
        due_date = borrow.borrow.time + datetime.timedelta(days=borrow.days)

        if due_date < datetime.datetime.now():
            mailer.send_reminder(
                borrow.borrower.first_name,
                borrow.borrower.user.email,
                borrow.borrow.carrier.identification
            )
