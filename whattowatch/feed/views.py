from collections import defaultdict
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ReviewListSerializer, ReviewSerializer
from .models import Review
from api.models import Movie
from accounts.models import UserReviewScore, UserLikeActors, UserLikeDirectors, UserLikeGenres
import numpy as np
from numpy import dot
from numpy.linalg import norm
from django.db.models import Q



@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        UserReviewScore.objects.create(review_user=request.user, review_movie=Movie.objects.get(id=request.data['movie_id']), score=request.data['score'])
        serializer = ReviewSerializer(data=request.data)
        movie = Movie.objects.get(id=request.data['movie_id'])

        for genre in movie.genres.all():
            ulg = UserLikeGenres.objects.filter(genre_like_user=request.user, genre=genre)

            if len(ulg):
                ulg = ulg[0]
                ulg.score += 1

            else:
                ulg = UserLikeGenres(genre=genre, genre_like_user=request.user, score=1)

            ulg.save()

        if serializer.is_valid(raise_exception=True):
            movie_id = request.data.get('movie_id')
            movie = Movie.objects.get(pk=movie_id)
            serializer.save(user=request.user, movie=movie)

            # 유저 유사도 계산 들어갈 자리
            user_eval = defaultdict(dict)
            # for reviewer in UserReviewScore.objects.all().distinct().values('review_user', 'score', 'review_movie'):
            for movie_id, score in UserReviewScore.objects.filter(review_user=request.user).distinct().values_list('review_movie', 'score'):
                print(movie_id, score,request.user.id )
                user_eval[request.user.id][movie_id] = score
            movie_ids = user_eval[request.user.id].keys()
            target_querys = UserReviewScore.objects.filter(~Q(review_user=request.user), review_movie__in=movie_ids)
            
            




            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_review_list(request, movie_pk):
    reviews = get_list_or_404(Review, movie=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
            
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # Review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        user_review_instance = UserReviewScore.objects.get(review_user=request.user, review_movie=request.data.movie_id)
        user_review_instance.delete()
        review.delete()

        # 유저 유사도 계산 들어갈 자리


        return Response({review_pk:'delete is success'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        user_review_instance = UserReviewScore.objects.get(review_user=request.user.id, review_movie=request.data.movie_id)
        user_review_instance.score = request.data.score
        user_review_instance.save()
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            # 유저 유사도 계산 들어갈 자리

            return Response(serializer.data)

