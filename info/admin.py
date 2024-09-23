from django.contrib import admin
from info import models

@admin.register(models.PersInfo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',]

