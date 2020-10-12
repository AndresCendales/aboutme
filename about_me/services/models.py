""" Services Model """

# Django 
from django.db import models


class Service(models.Model):
    """Service Model."""
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    picture = models.ImageField(
        upload_to='static/images/services/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    """Project Model."""
    name = models.CharField(max_length=50)
    description = models.TextField()
    picture = models.ImageField(
        upload_to='static/images/projects/',
        blank=True,
        null=True
    )
    link = models.CharField(max_length=50)
