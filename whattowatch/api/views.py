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
        print('OTT', i+1, '위')
        print('Netflix: ', end='')
        try:
            net_title = Movie.objects.get(title=netflix_title).title
            print(net_title)

        except:

            try:
                tmdb_id = R.find_id(title=netflix_title)
                tmdb_movie = Movie.objects.get(id=tmdb_id)
                tmdb_movie.title = netflix_title
                tmdb_movie.save()
                print(tmdb_movie.title, end='')
                print('(이름 달라서 db 수정)')
            except:
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
                print(movie.title, end='')
                print('(db에 없어서 TMDB에서 가져와 추가)')

        try:
            wat_title = Movie.objects.get(title=watcha_title).title
            print(wat_title)

        except:
            try:
                tmdb_id = R.find_id(title=watcha_title)       
                tmdb_movie = Movie.objects.get(id=tmdb_id)
                tmdb_movie.title = watcha_title
                tmdb_movie.save()
                print(tmdb_movie.title, end='')
                print('(이름 달라서 db 수정)')
            
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
                print(movie.title, end='')
                print('(db에 없어서 TMDB에서 가져와 추가)')
                
            


    # return render(request, 'index.html', context)

