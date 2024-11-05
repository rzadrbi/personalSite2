from django.core.exceptions import ValidationError
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
    picture = models.ImageField(upload_to='blogs')
    picture_2 = models.ImageField(blank=True, null=True, upload_to='blogs')
    picture_3 = models.ImageField(blank=True, null=True, upload_to='blogs')
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



class Comment(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='reply', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.name + '  --->  ' + self.body[:20]

    def clean(self):
        if self.parent and self.parent.parent:
            raise ValidationError('A comment with a parent cannot be a parent of another comment.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)