from django.shortcuts import render, redirect
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
        print('kir1')
        form.save()
        print('kir2')
        return super(ContactView, self).form_valid(form)

# def contact_view(request):
#     if request.method == 'POST':
#         form = forms.TiketForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             return redirect('info:main')  # Redirect after successful form submission
#     else:
#         form = forms.TiketForm()
#         return render(request, 'contact_us.html', {'form': form})
