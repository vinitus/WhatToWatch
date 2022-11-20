from django.urls import path, include
from . import views

app_name='api'
urlpatterns = [
    path('netflix/', views.netflix, name='netflix'),
    path('watcha/', views.watcha, name='watcha'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('directors/', views.director_list, name='director_list'),
    path('directors/<int:director_pk>/', views.director_detail, name='director_detail'),
    path('movies/search/<str:keyword>/', views.search, name='search'),
]