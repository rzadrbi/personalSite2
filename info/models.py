from django.db import models
import django_jalali.db.models as jmodels


class PersInfo(models.Model):
    name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='avatar')
    background = models.ImageField(upload_to='background')
    short_desc = models.TextField()
    long_desc = models.TextField()
    email = models.EmailField()
    tel_url = models.URLField()
    x_url = models.URLField()
    insta_url = models.URLField()
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    birthplace = models.TextField()

    def __str__(self):
        return self.name




