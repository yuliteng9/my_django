from django.db import models

# Create your models here.
class postProject(models.Model):
    codes = models.TextField()
    description = models.TextField(null=True, blank=True)