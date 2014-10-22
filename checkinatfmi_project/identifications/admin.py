import random
import string

from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

import checkinatfmi.translations_bg as translate

from models import Cardowner, Book, BookCategory
from checkinatfmi.mailer import send_welcome


class CardownerForm(forms.ModelForm):
    first_name = forms.CharField(label=translate.first_name)
    last_name = forms.CharField(label=translate.last_name)
    email = forms.EmailField(label=translate.email)

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
    search_fields = ('faculty_number',)

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


class CardownerProxy(Cardowner):
    class Meta:
        proxy = True
        app_label = 'university'
        verbose_name = translate.cardowner
        verbose_name_plural = translate.cardowners


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class BookProxy(Book):
    class Meta:
        proxy = True
        app_label = 'university'
        verbose_name = translate.book
        verbose_name_plural = translate.books


class BookCategoryAdmin(admin.ModelAdmin):
    pass

class BookCategoryProxy(BookCategory):
    class Meta:
        proxy = True
        app_label = 'university'
        verbose_name = translate.category
        verbose_name_plural = translate.categories

admin.site.register(CardownerProxy, CardownerAdmin)
admin.site.register(BookProxy, BookAdmin)
admin.site.register(BookCategoryProxy, BookCategoryAdmin)
