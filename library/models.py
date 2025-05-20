from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    is_available = models.BooleanField(default=True)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book = models.ManyToManyField(Books, related_name= 'author')

