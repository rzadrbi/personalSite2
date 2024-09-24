from django.urls import path
from django.views.generic import TemplateView
from info import views

app_name = 'info'

urlpatterns = [
    path('', views.indexView.as_view(), name='main'),
]


