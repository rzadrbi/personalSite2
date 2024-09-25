from django.db import models


class PersInfo(models.Model):
    name = models.CharField(max_length=120)
    short_desc = models.TextField()
    long_desc = models.TextField()
    email = models.EmailField()
    phone = models.BigIntegerField()
    birthday = models.DateField()
    birthplace = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اطلاعات شخصی'
        verbose_name_plural = verbose_name



