from __future__ import unicode_literals
from django.db import models
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def email_validate(self, email):
        return EMAIL_REGEX.match(email)
    def pw_validate(self, password, confirm):
        return password == confirm
# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
