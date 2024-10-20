from django.urls import path
from info import views

app_name = 'info'

urlpatterns = [
    path('', views.indexView.as_view(), name='main'),
]




