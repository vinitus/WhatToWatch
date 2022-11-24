from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Movie, Genre, Actor, Director
from django.utils.translation import gettext_lazy
from .managers import UserManager

# Create your models here.
# class User(AbstractUser):
#     gender = models.TextField()
#     like_genres = models.ManyToManyField(Genre, through='UserLikeGenres')    
#     like_actors = models.ManyToManyField(Actor, through='UserLikeActors')     
#     watched = models.ManyToManyField(Movie)
#     wishes = models.ManyToManyField(Movie, related_name="who_wishes")
#     user_similar = models.ManyToManyField('self', through='UserSimilar', symmetrical=True, default=0)
#     kakao_id = models.CharField(max_length=100, null=True)

class User(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    first_name = None
    last_name = None
    nickname = models.CharField(max_length=20, null=True)
    like_genres = models.ManyToManyField(Genre, through='UserLikeGenres')    
    like_actors = models.ManyToManyField(Actor, through='UserLikeActors')     
    watched = models.ManyToManyField(Movie)
    wishes = models.ManyToManyField(Movie, related_name="who_wishes")
    user_similar = models.ManyToManyField('self', through='UserSimilar', symmetrical=True, default=0)
    kakao_id = models.CharField(max_length=100, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

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

class UserSimilar(models.Model):
    score = models.IntegerField(default=0)
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='similar_user1')
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='similar_user2')

class UserReviewScore(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(null=True)
    
