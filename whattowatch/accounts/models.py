from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Movie, Genre, Actor

# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    birthday = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)
    like_genres = models.ManyToManyField(Genre)    
    like_actors = models.ManyToManyField(Actor)     
    watched = models.ManyToManyField(Movie)
