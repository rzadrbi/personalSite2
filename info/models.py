from django.db import models


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


class IDOInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.FileField(upload_to='icon')

    def __str__(self):
        return self.title

class Education(models.Model):
    name = models.CharField(max_length=120)
    years = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=120)
    years = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=120)
    percent = models.IntegerField()

    def __str__(self):
        return self.name
