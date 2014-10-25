
# -*- coding: utf-8 -*-

import smtplib
from django.core.mail import send_mail

import checkinatfmi.translations_bg as translate
from checkinatfmi.settings.keychain import *


WELCOME_TEMPLATE ="""Welcome at Checkin@FMI,
Hi %s, welcome to Checkin@FMI the checkin terminal of FMI.
Your username:
%s"
and password:
%s
Soon there will be login :)

Best Regards,
TheCodingMonkeys"""


REMINDER_TEMPLATE ="""
Hi $s,
We are sending you this email to remind you that your borrow - %s - is due today.
Please return it.

Best Regards,
TheCodingMonkeys"""


#def send_mail(to, subject, msg):
    #s=smtplib.SMTP_SSL()
    #s.connect(EMAIL_HOST, EMAIL_PORT)
    #s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    #message = 'Subject: %s \nTo: Me\n\n%s' % (subject, msg)
    #s.sendmail(EMAIL_HOST_USER, [to], message)


def send_welcome(name, email, username, password):
    subject = "Welcome to Checkin@FMI"
    msg = WELCOME_TEMPLATE % (name, username, password)
    send_mail(
        subject,
        welcome_msg,
        "thecodingmonkeys@gmail.com",
        [email]
    )


def send_reminder(name, email, item):
    subject = translate.borrow_reminder_subject
    msg = REMINDER_TEMPLATE % (name, item)
    send_mail(
        subject,
        msg,
        "thecodingmonkeys@gmail.com",
        [email]
    )


def send_borrow_invite(cardowner, book):
    subject = translate.borrow_invite_subject
    msg = translate.borrow_invite_template.format(cardowner.user.first_name, book.title)
    send_mail(
        subject,
        msg,
        "thecodingmonkeys@gmail.com",
        [cardowner.user.email]
    )
