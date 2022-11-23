from django.urls import path, include
from . import views

app_name='api'
urlpatterns = [
    path('netflix/', views.netflix, name='netflix'),
    path('watcha/', views.watcha, name='watcha'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/wishes/', views.movie_wishes, name='movie_wishes'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:director_pk>/', views.director_detail, name='director_detail'),
    path('user_interection/', views.user_interection, name='user_interection'),
    path('recommend_based_genres/', views.recommend_based_genres, name='recommend_based_genres'),
    path('recommend_based_actors/', views.recommend_based_actors, name='recommend_based_actors'),
    path('recommend_based_directors/', views.recommend_based_directors, name='recommend_based_directors'),
    path('watched/', views.watched, name='watched'),
    path('wishes/', views.wishes, name='wishes'),
    path('movies/search/<str:keyword>/', views.search, name='search'),
    path('movie_add/', views.movie_add, name='movie_add'),
    path('movie_title/', views.movie_title, name='movie_title'),
    path('provider/<int:movie_pk>/', views.provider, name='provider'),
]