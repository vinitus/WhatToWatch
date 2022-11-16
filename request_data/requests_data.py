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


    # 저장해둔 movie_list.json에서 id를 읽어와 detail 요청을 보내기
    def load_movie_detail(self):
        with open("./whattowatch/api/fixtures/movie_list.json", "r", encoding="UTF-8") as f:
            movie_list_json = json.load(f)

        movies_detail_json = []
        for movie in movie_list_json:
            movie_id = movie['id']

            MOVIE_DETAIL_API_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.API_KEY}&language=ko-KR'

            movie_detail_res = requests.get(MOVIE_DETAIL_API_URL)
            movie_detail_dict = json.loads(movie_detail_res.text)

            popular_movie_data = {"model": "api.movie"}
            popular_movie_data['fields'] = movie_detail_dict
            movies_detail_json.append(popular_movie_data)

            sleep(2)
            print(movie_id)
        print('end call')

        with open("./whattowatch/api/fixtures/movie_detail.json", "w", encoding="UTF-8") as outfile:
            json.dump(movies_detail_json, outfile, indent=4, ensure_ascii=False)

    
    # 장르 가져오기
    def load_genre(self):
        GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={self.API_KEY}&language=ko-KR'

        genres_res = requests.get(GENRE_URL)
        genres_res = json.loads(genres_res.text)

        genre_json = []
        # 원하는 JSON 형식으로 만들기 위한 가공
        for genre in genres_res['genres']:
            genre_data = {"model": "api.genre"}
            genre_data['id'] = genre['id']
            genre_data["fields"] = {}
            genre_data["fields"]["name"] = genre['name']
            genre_json.append(genre_data)
        
        print('end call')

        with open("./whattowatch/api/fixtures/genres.json", "w", encoding="UTF-8") as outfile:
            json.dump(genre_json, outfile, indent=4, ensure_ascii=False)

    # credit API 요청
    def load_credit(self):
        with open("./whattowatch/api/fixtures/movie_list.json", "r", encoding="UTF-8") as f:
            movie_list_json = json.load(f)

        credit_json = []
        for movie in movie_list_json:
            movie_id = movie['id']

            CREDIT_API_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={self.API_KEY}&language=ko-KR'

            credit_res = requests.get(CREDIT_API_URL)
            credit_dict = json.loads(credit_res.text)

            credit_json.append(credit_dict)
            print(movie_id)
            sleep(2)
        print('end call')

        with open("./whattowatch/api/fixtures/credit.json", "w", encoding="UTF-8") as outfile:
            json.dump(credit_json, outfile, indent=4, ensure_ascii=False)


RequestsData().load_movie_list()
RequestsData().load_movie_detail()
RequestsData().load_genre()
RequestsData().load_credit()
