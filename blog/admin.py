from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status', ]
    list_filter = ['status', 'publish', 'created', 'author', ]
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author', ]
    date_hierarchy = 'publish'
    ordering = ('-publish', 'status', )
    show_facets = admin.ShowFacets.ALWAYS


