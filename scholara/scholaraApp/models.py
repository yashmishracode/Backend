from django.db import models

# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)