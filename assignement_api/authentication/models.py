from django.db import models

# Create your models here.
class UserCredentials(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)