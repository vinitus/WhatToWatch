from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Movie, Genre, Actor

# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    birthday = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)
    like_genres = models.ManyToManyField(Genre, through='UserLikeGenres')    
    like_actors = models.ManyToManyField(Actor, through='UserLikeActors')     
    watched = models.ManyToManyField(Movie)

class UserLikeGenres(models.Model):
    genre_like_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True, default=0)
    
class UserLikeActors(models.Model):
    actor_like_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True, default=0)
