from django.db import models

# Create your models here.
class Technologie(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)