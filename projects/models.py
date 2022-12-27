from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_url = models.CharField(max_length=255)
    repository = models.CharField(max_length=255)
    technologies = models.ManyToManyField('technologies.Technologie', related_name='project')