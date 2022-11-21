from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Movie, Genre, Actor, Director

# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    birthday = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)
    like_genres = models.ManyToManyField(Genre, through='UserLikeGenres')    
    like_actors = models.ManyToManyField(Actor, through='UserLikeActors')     
    watched = models.ManyToManyField(Movie)
    # user_similar = models.ManyToManyField(User, through='UserSimilar', symmetrical=True)

class UserLikeGenres(models.Model):
    genre_like_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True, default=0)
    
class UserLikeActors(models.Model):
    actor_like_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True, default=0)

class UserLikeDirectors(models.Model):
    director_like_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True, default=0)

# class UserSimilar(models.Model):
#     score = models.IntegerField(null=True)
#     user_1 = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_2 = models.ForeignKey(User, on_delete=models.CASCADE)

class UserReviewScore(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True)
    
