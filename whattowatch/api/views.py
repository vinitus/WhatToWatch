from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie, Genre, Actor, Director
from accounts.models import User
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

# request.data['tmp'] == 'before': 유저에게 영화 선택지 보내기(popularity 높은 영화목록)
# request.data['tmp'] == 'after': 유저가 본 영화 정보 가져오기
@api_view(['POST'])
def user_interection(request):
    user = User.objects.get(id=request.data['user_pk'])
    watch_movies = user.watched.split()
    if request.data['tmp'] == 'before':          
        data = defaultdict(list)
        movies = Movie.objects.filter(popularity__gte=150)
        movies = movies.filter(vote_count__gte=50)
        
        # 유저가 이미 본 영화 거르기
        if user.watched:
            movies = movies.filter(~Q(id__in=watch_movies))

        for movie in movies:
            data['id'].append(movie.id)
            data['poster_path'].append(movie.poster_path)
            data['title'].append(movie.title)


        return Response(data)


    elif request.data['tmp'] == 'after':          
        like_genre = defaultdict(int)
        like_actor = defaultdict(int)
        watch_movies += request.data[movie_id]
        for movie_id, stat in zip(request.data['movie_id'], request.data['status']):
            
            if stat == 'watched':
                movie = Movie.objects.get(id=movie_id)
                for genre_instance in movie.genres.all():
                    like_genre[genre_instance.id] += 1
                    
                actors = Actor.objects.filter(movie=movie_id)
                for actor in actors:
                    like_actor[actor.pk] += 1
            
        like_genre_to_lst = []
        like_actor_to_lst = []
        for k in like_genre.keys():
            like_genre_to_lst.append((like_genre[k], k))
        for k in like_actor.keys():
            like_actor_to_lst.append((like_actor[k], k))
        like_genre_to_lst.sort(reverse=True)
        like_actor_to_lst.sort(reverse=True)
        
        like_genre_to_str = ''
        like_actor_to_str = ''
        
        for v, k in like_genre_to_lst:
            like_genre_to_str += f'{k}:{v} '

        for v, k in like_actor_to_lst:
            like_actor_to_str += f'{k}:{v} '
        
        user.watched = ' '.join(watch_movies)
        user.like_genres = like_genre_to_str
        user.like_actors = like_actor_to_str
        user.save()
        
        return HttpResponse(status.HTTP_200_OK)

# 유저 선택 정보에 따른 동일 장르 영화 추천
@api_view(['POST'])
def recommend_based_genres(request):
    user = User.objects.get(id=request.data['user_pk'])
    like_genres = []

    for genres in user.like_genres.split()[:2]:
        genre = genres.split(':')[0]
        like_genres.append(genre)
    movies = Movie.objects.filter(genres__in=[like_genres[0]])
    movies = movies.filter(genres__in=[like_genres[1]])
    movies = movies.filter(~Q(id__in=user.watched))
    movies = movies.filter(popularity__gte=100)
    movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
    return Response(movies)

# 유저 선택 정보에 따른 좋아하는 배우가 출연한 영화 추천
@api_view(['POST'])
def recommend_based_actors(request):
    user = User.objects.get(id=request.data['user_pk'])
    like_actors = []
    for actor in user.like_actors.split()[:2]:
        actor = actor.split(':')[0]
        like_actors.append(actor)
    movies = Movie.objects.filter(actors__in=[like_actors[0]])
    movies = movies.filter(~Q(id__in=user.watched))
    movies1 = movies.filter(actors__in=[like_actors[1]])
    if len(movies1) < 10:
        movies = json.load(serializers.serialize('json', movies, ensure_ascii=False))
        return Response(movies)
    else:
        movies1 = json.load(serializers.serialize('json', movies, ensure_ascii=False))
        return Response(movies1)

@api_view(['GET'])
def search(request, keyword):
    movies = get_list_or_404(Movie, title__contains=keyword)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
