from datetime import date

from django import forms


class BookSerachFrom(forms.Form):
    search = forms.CharField(required=False)
    from_year  = forms.IntegerField(required=False, initial="")
    to_year = forms.IntegerField(required=False, initial="")