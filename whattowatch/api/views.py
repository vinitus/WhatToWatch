from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie
from request_data.requests_data import RequestsData as R

# Create your views here.

# try except 지양, 현재 무비 모델과 장르 모델의 many to many field 처리 못해서 에러 나는 중..
def index(request):
    netflix_contents = NetflixTop10.objects.all()
    watcha_contents = WatchaTop10.objects.all()
    context = {
        'netflix_contents': netflix_contents,
        'watcha_contents': watcha_contents,
    }
    for i in range(10):
        netflix_title = netflix_contents[i].title
        watcha_title = watcha_contents[i].title
        print(i+1)
        try:
            net_title = Movie.objects.get(title=netflix_title).title
            print('넷플엔 있음! :', end=' ')
            print(net_title)

        except:
            print('넷플에 없어서 바꿈 !')
            tmdb_id = R.find_id(title=netflix_title)
            tmdb_movie = Movie.objects.get(id=tmdb_id)
            print(tmdb_movie.title, end=' ')
            tmdb_movie.title = netflix_title
            tmdb_movie.save()
            print(tmdb_movie.title)

        try:
            wat_title = Movie.objects.get(title=watcha_title).title
            print('왓차엔 있음! :', end=' ')
            print(wat_title)

        except:
            try:
                tmdb_id = R.find_id(title=watcha_title)       
                tmdb_movie = Movie.objects.get(id=tmdb_id)
                print('왓차에 없어서 바꿈 !')
                print(tmdb_movie.title, end=' ')
                tmdb_movie.title = watcha_title
                tmdb_movie.save()
                print(tmdb_movie.title)
            
            except:
                print('우리 DB에 없어서 TMDB에서 가져옴 !')
                tmdb_movie = R.request_movie_data(tmdb_id)

                movie = Movie(
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
                    # genres = tmdb_movie['genres'],
                    country = tmdb_movie['production_countries'][0]['name'],
                    belongs_to_collection = tmdb_movie['belongs_to_collection'],
                )
                movie.save()
                print(movie.title, end=' ')
                
            


    # return render(request, 'index.html', context)

