from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    birthday = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)