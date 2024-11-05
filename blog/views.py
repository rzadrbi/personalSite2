from django.shortcuts import render
from django.template.defaulttags import comment
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.filter(post=self.object)
        context['form'] = CommentForm()
        return context