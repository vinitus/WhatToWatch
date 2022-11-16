import json
import requests
from time import sleep
from secret import TMDB_API_KEY

class RequestsData:
    def __init__(self):
        self.API_KEY = TMDB_API_KEY
    
    # TMDB popular movie list 받아와서 json으로 저장
    def load_movie_list(self):
        movie_list_json = []

        for page in range(1,2):
            POPULAR_MOVIE_LIST_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={self.API_KEY}&language=ko-KR&page={page}'

            popular_movie_res = requests.get(POPULAR_MOVIE_LIST_URL)
            popular_movie_dict = json.loads(popular_movie_res.text)

            for popular_movie in popular_movie_dict['results']:
                movie_list_json.append(popular_movie)

            sleep(1.2)
            print(page)
        print('end call')
        with open("./whattowatch/api/fixtures/movie_list.json", "w", encoding="UTF-8") as outfile:
            json.dump(movie_list_json, outfile, indent=4, ensure_ascii=False)
