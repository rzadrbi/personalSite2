from django import forms
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):
    query = forms.CharField()
