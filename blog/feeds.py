from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords, truncatewords_html
from django.urls import reverse_lazy
import markdown as md
from blog.models import Post


class LatestPostFeed(Feed):
    title = "Reza Darabi"
    link = reverse_lazy("blog:blog_list")
    description = "New Posts of my Blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_extra_kwargs(self, item):
        return {'image_url': item.picture.url}

    def item_description(self, item):
        return truncatewords_html(md.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish