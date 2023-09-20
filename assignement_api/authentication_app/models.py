from django.db import models


class UserCredentials(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
# Create your models here.
