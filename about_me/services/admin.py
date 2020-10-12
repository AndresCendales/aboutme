""" Admin module for services """

# Django 
from django.contrib import admin

# Models
from .models import Service, Project


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Service admin"""

    list_display = (
        'name',
        'description',
        'picture',
    )

@admin.register(Project)
class ServiceAdmin(admin.ModelAdmin):
    """Project admin"""

    list_display = (
        'name',
        'description',
        'picture',
        'link'
    )
