from django.shortcuts import render
from django.views.generic import TemplateView
from info import models

class indexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        personal_info = models.PersInfo.objects.first()
        return dict(personal_info=personal_info)




