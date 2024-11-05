from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', ]
    list_filter = ['status', 'publish', 'created', 'author', ]
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author', ]
    date_hierarchy = 'publish'
    ordering = ('-publish', 'status', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'created', 'active',]
    list_filter = ['active', 'created',]
    search_fields = ['name', 'body',]

