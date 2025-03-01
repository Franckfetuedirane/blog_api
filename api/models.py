from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    # author = models.()

class author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    