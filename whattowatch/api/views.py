from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie, Genre, Actor, Director
from accounts.models import User, UserLikeActors, UserLikeGenres
from request_data.requests_data import RequestsData as R
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import GenreListSerializer, MovieListSerializer, ActorListSerializer, DirectorListSerializer, NetflixListSerializer, WatchaListSerializer
from django.db.models import Q
from collections import defaultdict
from django.http.response import HttpResponse
from django.core import serializers
import json
import random


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

# 
# GET: 유저에게 영화 선택지 보내기(popularity 높은 영화목록)
# POST: 유저가 본 영화 정보 가져오기
@api_view(['POST', 'GET'])
def user_interection(request):
    print(request.user)
    user = User.objects.get(id=request.user.id)
    watch_movies = []
    for movie in user.watched.all():
        watch_movies.append(movie.id)
    if request.method == 'GET':          
        datas = []
        movies = Movie.objects.filter(popularity__gte=150)
        movies = movies.filter(vote_count__gte=50)
        
        # 유저가 이미 본 영화 거르기
        if user.watched:
            movies = movies.filter(~Q(id__in=watch_movies))

        for movie in movies:
            data = {}
            data['id'] = movie.id
            data['poster_path'] = movie.poster_path
            data['title'] = movie.title
            data['popularity'] = movie.popularity
            datas.append(data)
        datas.sort(key=lambda x: x['popularity'], reverse=True)

        return Response(datas)


    elif request.method == 'POST':          

        for movie_id in request.data['movie_id']:
            movie = Movie.objects.get(id=movie_id)
            user.watched.add(movie)
            for genre_instance in movie.genres.all():
                # print('#'*40)
                # print(genre_instance.id)
                user_like_genres = UserLikeGenres.objects.filter(genre_like_user=request.user, genre=genre_instance)
                if len(user_like_genres) == 0:
                    user_like_genres = UserLikeGenres.objects.create(genre_like_user=request.user, genre=genre_instance)
                else:
                    user_like_genres = user_like_genres[0]
                # print(user_like_genres)
                # print('#'*40)
                user_like_genres.score += 1
                user_like_genres.save()
            actors = Actor.objects.filter(movies=movie_id)
            for actor in actors:
                # print(actor)
                # print('#'*40)
                user_like_actor = UserLikeActors.objects.filter(actor_like_user=request.user, actor=actor)
                if len(user_like_actor) == 0:
                    user_like_actor = UserLikeActors.objects.create(actor_like_user=request.user, actor=actor)
                    user_like_actor.score = 1
                else:
                    user_like_actor = user_like_actor[0]
                    # print(user_like_actor)
                    user_like_actor.score += 1
                # print(user_like_actor.score)
                user_like_actor.save()
            # print(user)
        user.save()
        
        return HttpResponse(status.HTTP_200_OK)

# 유저 선택 정보에 따른 동일 장르 영화 추천
@api_view(['GET'])
def recommend_based_genres(request):
    user = User.objects.get(id=request.user.id)
    like_genres = UserLikeGenres.objects.filter(genre_like_user=user).order_by('-score')
    movies = Movie.objects.filter(genres__in=[like_genres[0].genre_id])
    movies = movies.filter(popularity__gte=100)
    movies = movies.filter(genres__in=[like_genres[1].genre_id])
    user_watched = []
    for movie in user.watched.all():
        user_watched.append(movie.id) 
    movies = movies.filter(~Q(id__in=user_watched))
    movies1 = movies.filter(genres__in=[like_genres[2].genre_id])
    if len(movies1) < 10:
        movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
        return Response(movies)
    else:
        print(len(movies1))
        movies1 = json.loads(serializers.serialize('json', movies1, ensure_ascii=False))
        print(movies1)
        return Response(movies1)


# 유저 선택 정보에 따른 좋아하는 배우가 출연한 영화 추천
@api_view(['GET'])
def recommend_based_actors(request):
    user = User.objects.get(id=request.user.id)
    like_actors = UserLikeActors.objects.filter(actor_like_user=user).order_by('-score')
    movies = Movie.objects.filter(actor__in=[like_actors[0].actor_id])
    user_watched = []
    for movie in user.watched.all():
        user_watched.append(movie.id) 
    movies = movies.filter(~Q(id__in=user_watched))
    movies1 = movies.filter(actor__in=[like_actors[1].actor_id])
    movies2 = movies1.filter(actor__in=[like_actors[2].actor_id])
    if len(movies1) < 10:
        print(like_actors[0].actor_id)
        print(Actor.objects.get(id=like_actors[0].actor_id).name)
        movies = movies.filter(popularity__gte=50)
        movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
        return Response(movies)
    else:
        movies2 = json.loads(serializers.serialize('json', movies1, ensure_ascii=False))
        return Response(movies2)

        
@api_view(['GET'])
def search(request, keyword):
    movies = get_list_or_404(Movie, title__contains=keyword)
    movies.sort(key=lambda x: x.popularity, reverse=True)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_add(request):
    movie = Movie()
    print(request.text)
    return HttpResponse(status.HTTP_201_CREATED)