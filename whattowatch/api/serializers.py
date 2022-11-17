from rest_framework import serializers
from .models import Movie, Genre, Actor, Director


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class DirectorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'