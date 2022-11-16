from django.contrib import admin
from . import models

@admin.register(models.Project)
class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']


@admin.register(models.Tag)
class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(models.Review)
class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ['project', 'body', 'value']