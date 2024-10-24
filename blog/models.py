from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    caption = models.TextField()
    caption_2 = models.TextField()
    picture = models.ImageField()
    picture_2 = models.ImageField(blank=True, null=True)
    picture_3 = models.ImageField(blank=True, null=True)
    summery_title = models.CharField(max_length=250)
    summery_text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['publish'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',
                       args=[self.slug,
                             ])

    # def show_image1(self):
    #     if self.picture1:
    #         return format_html(
    #             f'<img src="{self.picture1.url}" alt="{self.title}" style="max-width: 200px; max-height: 200px;">')
    #
    # return "No Image"
    #
    # def show_image2(self):
    #     if self.picture2:
    #         return format_html(
    #             f'<img src="{self.picture2.url}" alt="{self.title}" style="max-width: 200px; max-height: 200px;">')
    #
    # return "No Image"
    #
    # def show_image3(self):
    #     if self.picture3:
    #         return format_html(
    #             f'<img src="{self.picture3.url}" alt="{self.title}" style="max-width: 200px; max-height: 200px;">')
    #
    # return "No Image"
