from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    number = models.IntegerField()

class Quote(models.Model):
    author = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default="quote-1")
    text = models.TextField()
