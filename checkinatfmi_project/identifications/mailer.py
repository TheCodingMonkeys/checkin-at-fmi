import smtplib
from django.core.mail import send_mail

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



#def send_mail(to, subject, msg):
    #s=smtplib.SMTP_SSL()
    #s.connect(EMAIL_HOST, EMAIL_PORT)
    #s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    #message = 'Subject: %s \nTo: Me\n\n%s' % (subject, msg)
    #s.sendmail(EMAIL_HOST_USER, [to], message)


def send_welcome(name, email, username, password):
    subject = "Welcome to Checkin@FMI"
    welcome_msg = WELCOME_TEMPLATE % (name, username, password)
    send_mail(
	subject,
	welcome_msg,
	"thecodingmonkeys@gmail.com",
	[email])
