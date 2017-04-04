from __future__ import unicode_literals
from django.db import models
from ..validate.models import User

class Book(models.Model):
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.CharField(max_length=5)
    poster = models.ForeignKey(User, related_name='review_user')
    book = models.ForeignKey(Book, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
