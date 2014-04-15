import random
import string

from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

from models import Cardowner, Book
from mailer import send_welcome

class CardownerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if not 'instance' in kwargs:
            return

        user = kwargs['instance'].user
        if user:
            first_name = user.first_name
            last_name = user.last_name
            email = user.email

            self.initial['first_name']=first_name
            self.initial['last_name']=last_name
            self.initial['email']=email

    class Meta:
        model = Cardowner
        exclude = ['user', 'carrier']

class CardownerAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'last_name',
        'email',
        'faculty_number',
        'grade',
        'specialty',
    )

    form = CardownerForm
    
    def save_model(self, request, obj, form, change):
        password = None
        faculty_number = form.cleaned_data['faculty_number']
        if hasattr(obj, 'user'):
            user = obj.user
        else:
            user = User.objects.get_or_create(username=faculty_number)[0]
            password = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for x in range(7)
            )

        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.username = faculty_number

        if password:
            #send_welcome(
            #    user.first_name,
            #    user.email,
            #    user.username,
            #    password
            #)
            user.set_password(password)

        user.save()
        obj.user = user
        obj.save()


admin.site.register(Cardowner, CardownerAdmin)
admin.site.register(Book)

