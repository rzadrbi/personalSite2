from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('list', PostListView.as_view(), name='blog_list'),
]

