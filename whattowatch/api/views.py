from django.shortcuts import render
from .models import NetflixTop10, WatchaTop10, Movie


# Create your views here.
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
            print('넷플에 없어서 바꿈 ! :', end=' ')
            tmdb_id = find_id(netflix_title)
            tmdb_movie = Movie.objects.get(id=tmdb_id)
            tmdb_movie.title = netflix_title
            tmdb_movie.save()
            print(tmdb_movie.title)

        try:
            wat_title = Movie.objects.get(title=watcha_title).title
            print('왓차엔 있음! :', end=' ')
            print(wat_title)

        except:
            print('왓차에 없어서 바꿈 ! :', end=' ')
            tmdb_id = find_id(watcha_title)
            tmdb_movie = Movie.objects.get(id=tmdb_id)
            print('11111')
            print(tmdb_movie)
            tmdb_movie.title = watcha_title
            tmdb_movie.save()
            print(tmdb_movie.title)


    # return render(request, 'index.html', context)

