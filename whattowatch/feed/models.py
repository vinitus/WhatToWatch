from django.db import models

# Create your models here.
class Review(models.Model):
    content =  models.TextField()
    score = models.FloatField()
    watched = models.BooleanField()
    