from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.TextField()
    gender = models.TextField()
    birthday = models.DateField()
    phone_number = models.IntegerField()