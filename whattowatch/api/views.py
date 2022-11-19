from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie, Genre, Actor, Director
from request_data.requests_data import RequestsData as R
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import GenreListSerializer, MovieListSerializer, ActorListSerializer, DirectorListSerializer, NetflixListSerializer, WatchaListSerializer
from django.db.models import Q


@api_view(['GET'])
def netflix(request):
    netflix_contents = NetflixTop10.objects.all()

    for i in range(10):
        netflix_title = netflix_contents[i].title

        # print('OTT', i+1, '위')
        # print('Netflix: ', end='')
        try:
            net_title = Movie.objects.get(title=netflix_title).title
            # print(net_title)

        except:

            try:
                tmdb_id = R.find_id(title=netflix_title)
                tmdb_movie = Movie.objects.get(id=tmdb_id)
                tmdb_movie.title = netflix_title
                tmdb_movie.save()
                # print(tmdb_movie.title, end='')
                # print('(이름 달라서 db 수정)')
            except:
                tmdb_id = R.find_id(title=netflix_title)
                tmdb_movie = R.request_movie_data(tmdb_id)
                tmdb_genres = []
                for i in range(len(tmdb_movie['genres'])):
                    tmdb_genres.append(tmdb_movie['genres'][i]['id'])
                movie = Movie.objects.create(
                    title = netflix_title,
                    overview = tmdb_movie['overview'],
                    poster_path = tmdb_movie['poster_path'],
                    popularity = tmdb_movie['popularity'],
                    release_date = tmdb_movie['release_date'],
                    runtime = tmdb_movie['runtime'],
                    vote_average = tmdb_movie['vote_average'],
                    vote_count = tmdb_movie['vote_count'],
                    backdrop_path = tmdb_movie['backdrop_path'],
                    original_language = tmdb_movie['original_language'],
                    adult = tmdb_movie['adult'],
                    country = tmdb_movie['production_countries'][0]['name'],
                    belongs_to_collection = tmdb_movie['belongs_to_collection']['id'] if tmdb_movie['belongs_to_collection'] else None,
                )
                movie.genres.set(tmdb_genres)
                movie.save()
                # print(movie.title, end='')
                # print('(db에 없어서 TMDB에서 가져와 추가)')

    netflix = get_list_or_404(NetflixTop10)
    data = []
    for i in range(10):        
        movie_list = Movie.objects.filter(title=netflix[i].title)
        if len(movie_list) != 1:
            for movie in movie_list:
                if movie.release_date[:4] == netflix[i].release_date:
                    break
        else:
            movie = movie_list[0]
        movie_info = {
            'movie_id': movie.id,
            'poster_path': movie.poster_path,
            'title': netflix[i].title,
            'country': movie.country,
            'year': netflix[i].release_date,
            'rank': netflix[i].rank
        }
        data.append(movie_info)
    return Response(data)

@api_view(['GET'])
def watcha(request):
    watcha_contents = WatchaTop10.objects.all()

    for i in range(10):
        watcha_title = watcha_contents[i].title
        try:
            wat_title = Movie.objects.get(title=watcha_title).title
            # print(wat_title)

        except:
            try:
                tmdb_id = R.find_id(title=watcha_title)       
                tmdb_movie = Movie.objects.get(id=tmdb_id)
                tmdb_movie.title = watcha_title
                tmdb_movie.save()
                # print(tmdb_movie.title, end='')
                # print('(이름 달라서 db 수정)')
            
            except:
                tmdb_movie = R.request_movie_data(tmdb_id)
                tmdb_genres = []
                for i in range(len(tmdb_movie['genres'])):
                    tmdb_genres.append(tmdb_movie['genres'][i]['id'])
                movie = Movie.objects.create(
                    title = watcha_title,
                    overview = tmdb_movie['overview'],
                    poster_path = tmdb_movie['poster_path'],
                    popularity = tmdb_movie['popularity'],
                    release_date = tmdb_movie['release_date'],
                    runtime = tmdb_movie['runtime'],
                    vote_average = tmdb_movie['vote_average'],
                    vote_count = tmdb_movie['vote_count'],
                    backdrop_path = tmdb_movie['backdrop_path'],
                    original_language = tmdb_movie['original_language'],
                    adult = tmdb_movie['adult'],
                    country = tmdb_movie['production_countries'][0]['name'],
                    belongs_to_collection = tmdb_movie['belongs_to_collection']['id'] if tmdb_movie['belongs_to_collection'] else None,
                )
                movie.genres.set(tmdb_genres)
                movie.save()
                # print(movie.title, end='')
                # print('(db에 없어서 TMDB에서 가져와 추가)')             

    watcha = get_list_or_404(WatchaTop10)
    data = []
    for i in range(10):
        movie_list = Movie.objects.filter(title=watcha[i].title)
        if len(movie_list) != 1:
            for movie in movie_list:
                if movie.release_date[:4] == watcha[i].release_date:
                    break
        else:
            movie = movie_list[0]
        movie_info = {
            'movie_id': movie.id,
            'poster_path': movie.poster_path,
            'title': watcha[i].title,
            'country': movie.country,
            'year': watcha[i].release_date,
            'rank': watcha[i].rank
        }
        data.append(movie_info)
    return Response(data)
            

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)
    # genres = get_list_or_404(Genre)
    # date = {}
    # for genre in genres:
    #     # print(dir(genre))
    #     print(genre.movie_set.count(), genre.name)
    

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreListSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorListSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def director_list(request):
    directors = get_list_or_404(Director)
    serializer = DirectorListSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def director_detail(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)
    serializer = DirectorListSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
def search(request, keyword):
    movies = get_list_or_404(Movie, title__contains=keyword)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)