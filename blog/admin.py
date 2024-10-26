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
    list_display = ['get_username', 'get_user_email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['user__username', 'user__email', 'body']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'User Name'

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'User Email'
