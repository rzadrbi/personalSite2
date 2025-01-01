from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView
from info import models, forms


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


class ContactView(FormView):
    template_name = 'contact_us.html'
    form_class = forms.TiketForm
    success_url = '/'
    def form_valid(self, form):
        send_mail('تایید دریافت پیام',
                  f"""    {form.cleaned_data.get('name')} عزیز 
                   پیام شما دریافت شد و در اسرع وقت پاسخ داده خواهد شد
                    rezadarabi.ir""",
                  'rezadaraiofficially@gmail.com',
                  [str(form.cleaned_data.get('email'))],
                  fail_silently=False)
        print('kir')
        form.save()
        return super(ContactView, self).form_valid(form)


class Handler404(TemplateView):
    template_name = '404.html'

