from django.core.mail import send_mail


WELCOME_TEMPLATE ="""Welcome at Checkin@FMI",
"Hi %s, welcome to Checkin@FMI the checkin terminal ofFMI.
Your username is "%s" and password "%s",
please be sure to change your password as soon as posible!
Best Regards,
TheCodingMonkeys""" 

def send_welcome(name, email, username, password):
    send_mail("Welcome to Checkin@FMI",
                WELCOME_TEMPLATE % (name, username, password),
                'thecodingmonkeys@gmail.com',
                [email],
                fail_silently=False)
