from django.urls import path
from info import views

app_name = 'info'

urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('resume', views.ResumeView.as_view(), name='Resume'),
]




