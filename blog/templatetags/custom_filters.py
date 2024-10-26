import datetime
from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def time_since(value):
    if not value:
        return ""

    now_time = now()
    diff = now_time - value

    if diff.days >= 365:
        return f"{diff.days // 365} سال پیش"
    if diff.days >= 30:
        return f"{diff.days // 30} ماه پیش"
    if diff.days >= 1:
        return f"{diff.days} روز پیش"
    if diff.seconds >= 3600:
        return f"{diff.seconds // 3600} ساعت پیش"
    if diff.seconds >= 60:
        return f"{diff.seconds // 60} دقیقه پیش"
    return "چند لحظه پیش"