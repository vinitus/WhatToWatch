from django.urls import path
from . import views

app_name = 'feed'
urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/movie/<int:movie_pk>/', views.movie_review_list),
]

