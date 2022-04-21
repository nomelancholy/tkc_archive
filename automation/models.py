from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    release_year = models.IntegerField()
    featured = models.CharField(max_length=100)
    comment = models.TextField()
    status = models.CharField(max_length=5)