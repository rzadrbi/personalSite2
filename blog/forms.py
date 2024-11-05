from django import forms
from django.core.exceptions import ValidationError
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'gender',]

        widgets = {
            'gender': forms.RadioSelect(choices=Comment.GENDER_CHOICES, attrs={'class': 'selection'}),
            'body': forms.Textarea(attrs={'class': 'form-control textarea',
                                          'placeholder':'نظر خود را اینجا بنویسید',
                                          'required':'required', 'rows':5}),
            'name': forms.TextInput(attrs={'class': 'form-control textarea',
                                           'placeholder': 'نام'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
