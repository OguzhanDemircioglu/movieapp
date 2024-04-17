from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

class Movie(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.CharField(max_length=100)
  anasayfa = models.BooleanField(default=False)


