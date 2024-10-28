from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, url_name):
        if str(resolve(context.request.path_info).url_name) == str(url_name):
            return 'active'
        return ''

