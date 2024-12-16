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
            'email': forms.EmailInput(attrs={'class': "form-control",
                                           'type': "email",
                                           'placeholder': "ایمیل",
                                           'id': "emailContact",
                                           'name': "emailContact",
                                           'required': "required",
                                           'autocomplete': "on",
                                           'oninvalid': "setCustomValidity('ایمیل نادرست است')",
                                           'onkeyup': "setCustomValidity('')",}),
            'body' : forms.TextInput(attrs={'class': "textarea form-control",
                                            'type': "text",
                                            'placeholder': "پیام...",
                                            'id': "messageContact",
                                            'name': "messageContact",
                                            'required': "required",
                                            'autocomplete': "on",
                                            'rows': "4",
                                            'oninvalid': "setCustomValidity('فیلد را پر کنید')",
                                            'onkeyup': "setCustomValidity('')",
                                            })

        }
