import smtplib

from checkinatfmi.settings.keychain import *


WELCOME_TEMPLATE ="""Welcome at Checkin@FMI,
Hi %s, welcome to Checkin@FMI the checkin terminal of FMI.
Your username is "%s" and password "%s",
please be sure to change your password as soon as posible!

Best Regards,
TheCodingMonkeys""" 



def send_mail(to, subject, msg):
    s=smtplib.SMTP_SSL()
    s.connect("smtp.gmail.com",EMAIL_PORT)
    s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    message = 'Subject: %s \nTo: Me\n\n%s' % (subject, msg)
    s.sendmail(EMAIL_HOST_USER, [to], message)


def send_welcome(name, email, username, password):
    subject = "Welcome to Checkin@FMI"
    welcome_msg = WELCOME_TEMPLATE % (name, username, password)
    send_mail(email, subject, welcome_msg)
