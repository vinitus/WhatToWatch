from rest_framework import serializers
from .models import Movie, Genre, Actor, Director, NetflixTop10, WatchaTop10
from accounts.models import User

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


class NetflixListSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetflixTop10
        fields = '__all__'


class WatchaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchaTop10
        fields = '__all__'
