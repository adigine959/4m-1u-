from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

class Hashtag(models.Model):
    title = models.CharField(max_length=256)
