from django.shortcuts import render
from django.views.generic import TemplateView
from info import models

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        personal_info = models.PersInfo.objects.first()
        ido = models.IDOInfo.objects.all()
        return dict(info=personal_info, ido=ido)

class ResumeView(TemplateView):
    template_name = 'resume.html'
    def get_context_data(self, **kwargs):
        return dict(edu=models.Education.objects.all(),
                    exp=models.Experience.objects.all(),
                    skl=models.Skill.objects.all())
