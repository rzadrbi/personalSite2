from django.urls import path
from info import views

app_name = 'blog'

urlpatterns = [
    path('list', views, name='blog_list'),
]

