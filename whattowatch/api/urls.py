<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
]
=======
from django.urls import path, include
from . import views

app_name='api'
urlpatterns = [
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
]
>>>>>>> bf8c2e7808de8f109bd4d7ecd084d718e924e923
