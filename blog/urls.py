from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import *
from blog.sitemaps import PostSitemap
from blog.feeds import LatestPostFeed

sitemaps = {
    'posts': PostSitemap,
}

app_name = 'blog'

urlpatterns = [
    path('list', PostListView.as_view(), name='blog_list'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('tag/<slug:tag_slug>', PostListView.as_view(), name='blog_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', PostDetailView.as_view(), name='detail'),
    path('feed/', LatestPostFeed(), name='post_feed'),
]

