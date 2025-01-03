import requests
from allauth.socialaccount.internal.flows.connect import connect
from django.db.models import Count
from django.views.generic import ListView, DetailView, TemplateView
from taggit.models import Tag

from blog.models import Post


class PostListView(TemplateView):
    template_name = 'blog_list.html'

    def get_context_data(self, **kwargs):
        tags = Tag.objects.all()
        posts = Post.objects.all()
        tag = self.kwargs.get('tag_slug')
        if tag:
            posts = posts.filter(tags__name__contains=tag)
        return dict(tags=tags, posts=posts, tag=tag)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
        context['similar_posts'] = similar_posts.annotate(same_tags_count=Count('tags')).order_by('-same_tags_count',
                                                                                                  '-publish')[:4]
        return context

