from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    content =  models.TextField()
    score = models.FloatField()
    watched = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey('api.Movie', on_delete=models.CASCADE)