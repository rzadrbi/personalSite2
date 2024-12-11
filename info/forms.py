from django import forms
from info import models as local_model

class TiketForm(forms.ModelForm):
    class Meta:
        model = local_model.Ticket
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control",
                                           'type': "text",
                                           'placeholder': "نام و نام خانوادگی",
                                           'id': "nameContact",
                                           'name': "nameContact",
                                           'required': "required",
                                           'autocomplete': "on",
                                           'oninvalid': "setCustomValidity('پر کردن این فیلد ضروری است.')",
                                           'onkeyup': "setCustomValidity('')",}),
            'email': forms.EmailField(attrs={'class': "form-control",
                                           'type': "text",
                                           'placeholder': "نام و نام خانوادگی",
                                           'id': "nameContact",
                                           'name': "nameContact",
                                           'required': "required",
                                           'autocomplete': "on",
                                           'oninvalid': "setCustomValidity('پر کردن این فیلد ضروری است.')",
                                           'onkeyup': "setCustomValidity('')",})

        }