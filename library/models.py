from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    is_available = models.BooleanField(default=True)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book = models.ManyToManyField(Books, related_name= 'author')

class Order(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today())
    return_date = models.DateField(null=True, blank=True)
