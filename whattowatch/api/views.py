from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie, Genre, Actor, Director
from accounts.models import User, UserLikeActors, UserLikeGenres, UserLikeDirectors, UserReviewScore
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
import pandas as pd
import numpy as np
import math




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

@api_view(['GET','POST'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        movie = Movie.objects.get(id=movie_pk)
        if not user.watched.filter(pk=movie_pk):
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
            actors = Actor.objects.filter(movies=movie_pk)
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
            user.save()
            return Response({movie_pk:True})
        else:
            user.watched.remove(movie)
            for genre_instance in movie.genres.all():
                user_like_genres = UserLikeGenres.objects.get(genre_like_user=request.user, genre=genre_instance)
                user_like_genres.score -= 1    
                user_like_genres.save()
            actors = Actor.objects.filter(movies=movie_pk)
            for actor in actors:
                user_like_actor = UserLikeActors.objects.get(actor_like_user=request.user, actor=actor)
                user_like_actor.score -= 1    
                user_like_actor.save()
            user.save()
            return Response({movie_pk:False})

@api_view(['GET'])
def movie_title(request):
    with open("./api/fixtures/movie_titles.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    return Response(data)

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

            directors = Director.objects.filter(movies=movie_id)
            for director in directors:
                # print(actor)
                # print('#'*40)
                user_like_director = UserLikeDirectors.objects.filter(director_like_user=request.user, director=director)
                if len(user_like_director) == 0:
                    user_like_director = UserLikeDirectors.objects.create(director_like_user=request.user, director=director)
                    user_like_director.score = 1
                else:
                    user_like_director = user_like_director[0]
                    # print(user_like_director)
                    user_like_director.score += 1
                # print(user_like_director.score)
                user_like_director.save()
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

    movie_dict = {'genre':Genre.objects.get(id=like_genres[0].genre_id).name}
    if len(movies1) < 10:
        movies = movies.filter(popularity__gte=50)
        movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
        movie_dict['movies'] = movies
    else:
        movies2 = json.loads(serializers.serialize('json', movies1, ensure_ascii=False))
        movie_dict['movies'] = movies2
    for movie in movie_dict['movies']:
        movie['postter_path'] = Movie.objects.get(pk=movie['pk']).poster_path
        movie['movie_id'] = movie.pop('pk')
        movie_field = movie.pop('fields')
        movie['title'] = movie_field['title']
        movie['poster_path'] = movie_field['poster_path']
    return Response(movie_dict)


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
    movie_dict = {'actor': Actor.objects.get(id=like_actors[0].actor_id).name}
    if len(movies1) < 10:
        movies = movies.filter(popularity__gte=50)
        movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
        movie_dict['movies'] = movies
    else:
        movies2 = json.loads(serializers.serialize('json', movies1, ensure_ascii=False))
        movie_dict['movies'] = movies2
    for movie in movie_dict['movies']:
        movie['postter_path'] = Movie.objects.get(pk=movie['pk']).poster_path
        movie['movie_id'] = movie.pop('pk')
        movie_field = movie.pop('fields')
        movie['title'] = movie_field['title']
        movie['poster_path'] = movie_field['poster_path']
    return Response(movie_dict)

@api_view(['GET'])
def recommend_based_directors(request):
    user = User.objects.get(id=request.user.id)
    like_director = UserLikeDirectors.objects.filter(director_like_user=user).order_by('-score')

    movies = Movie.objects.filter(director__in=[like_director[0].director_id])
    user_watched = []
    for movie in user.watched.all():
        user_watched.append(movie.id)
    movies = movies.filter(~Q(id__in=user_watched))
    # movies = movies.filter(director__in=[like_director[1].director_id])
    if len(movies) == 0:
        return Response({'director':None, 'movies':[]})
    
    movie_dict = {'director': Director.objects.get(id=like_director[0].director_id).name}
    movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
    movie_dict['movies'] = movies
    for movie in movie_dict['movies']:
        movie['postter_path'] = Movie.objects.get(pk=movie['pk']).poster_path
        movie['movie_id'] = movie.pop('pk')
        movie_field = movie.pop('fields')
        movie['title'] = movie_field['title']
        movie['poster_path'] = movie_field['poster_path']
    return Response(movie_dict)

def cosim(name, dataframe):
    movies = []
    for i in dataframe.loc[name,:].index:

        if math.isnan(dataframe.loc[name,i]) == False:
            movies.append(i)
    U_df = pd.DataFrame(dataframe.loc[name,movies] ).T
    
    other_df=dataframe.loc[:,movies].drop(name, axis=0)
    
    U_list= list(U_df.index)
    
    sim_dict={}
    
    
    for user in other_df.index:
        sm= [m for m in U_df.columns if math.isnan(other_df.loc[user,m])==False]
        
        main_n = np.linalg.norm(U_df.loc[name,sm])
        user_n = np.linalg.norm(other_df.loc[user,sm])
        prod = np.dot(U_df.loc[name,sm], other_df.loc[user,sm])
        sim_dict[user]=prod/(main_n*user_n)
        
    
    return sim_dict


@api_view(['GET'])
def recommend_based_users(request):
    user_eval = defaultdict(dict)
    # for reviewer in UserReviewScore.objects.all().distinct().values('review_user', 'score', 'review_movie'):
    for user_id, movie_id, score in UserReviewScore.objects.all().distinct().values_list('review_user', 'review_movie', 'score'):
        user_eval[user_id][movie_id] = score
    
    user_review_datas = pd.DataFrame(user_eval).T
    # target_querys = UserReviewScore.objects.filter(~Q(review_user=request.user), review_movie__in=movie_id)
    user_similar = cosim(request.user.id, user_review_datas)
    user_sims = []
    for k, v in user_similar.items():
        if v < 0.94:
            continue
        user_sims.append(k)
    recommend_movies = []
    review_movies = []
    for movie in User.objects.get(id=request.user.id).watched.all():
        review_movies.append(movie.id)
    if user_sims:
        for user_sim in user_sims:
            reco_movies = UserReviewScore.objects.filter(~Q(review_movie__in=review_movies), review_user=user_sim, score__gte=8).distinct().values('review_movie')
            for reco_movie in reco_movies:
                recommend_movies.append(reco_movie['review_movie'])
    movies = Movie.objects.filter(id__in=recommend_movies)
    movie_dict = {'user': '고객님과 취향이 비슷한 유저'}
    movies = json.loads(serializers.serialize('json', movies, ensure_ascii=False))
    movie_dict['movies'] = movies
    for movie in movie_dict['movies']:
        movie['postter_path'] = Movie.objects.get(pk=movie['pk']).poster_path
        movie['movie_id'] = movie.pop('pk')
        movie_field = movie.pop('fields')
        movie['title'] = movie_field['title']
        movie['poster_path'] = movie_field['poster_path']
    return Response(movie_dict)
    


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