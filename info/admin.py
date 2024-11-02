from django.contrib import admin
from info import models

@admin.register(models.PersInfo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',]


@admin.register(models.IDOInfo)
class IDOInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]


