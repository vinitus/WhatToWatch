from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField(null=True)
    popularity = models.FloatField()
    release_date = models.TextField()
    runtime = models.IntegerField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    backdrop_path = models.TextField()
    original_language = models.TextField()
    adult = models.BooleanField()
    genres = models.ManyToManyField(Genre)
    country = models.CharField(max_length=30)
    belongs_to_collection = models.IntegerField(null=True)

<<<<<<< HEAD
class NetflixTop10(models.Model):
    rank = models.IntegerField()
    title = models.TextField()
    release_date = models.TextField()
    
class WatchaTop10(models.Model):
    rank = models.IntegerField()
    title = models.TextField()
    release_date = models.TextField()
=======
class Director(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
>>>>>>> bf8c2e7808de8f109bd4d7ecd084d718e924e923
