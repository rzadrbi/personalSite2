from django.contrib import admin
from info import models

@admin.register(models.PersInfo)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',]


@admin.register(models.IDOInfo)
class IDOInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]

@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',]


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percent',]

