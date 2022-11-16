import json
import requests
from time import sleep
from .secret import TMDB_API_KEY

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
            genre_data['pk'] = genre['id']
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

    # TMDB movie detail response 형식 바꾸기
    def transform_movie_detail_json(self):
        with open("./whattowatch/api/fixtures/movie_detail.json", "r", encoding="UTF-8") as f:
            movie_detail_json = json.load(f)

        for idx in range(len(movie_detail_json)):
            movie_detail_json[idx]['fields'].pop('backdrop_path')
            if movie_detail_json[idx]['fields']['belongs_to_collection']:
                movie_detail_json[idx]['fields']['belongs_to_collection'] = movie_detail_json[idx]['fields']['belongs_to_collection']['id']
            movie_detail_json[idx]['fields'].pop('budget')
            movie_detail_json[idx]['fields'].pop('homepage')
            genre_list = movie_detail_json[idx]['fields'].pop('genres')
            movie_detail_json[idx]['fields']['genres'] = []
            for genre in genre_list:
                movie_detail_json[idx]['fields']['genres'].append(genre['id'])
            movie_detail_json[idx]['fields'].pop('imdb_id')
            movie_detail_json[idx]['fields'].pop('original_title')
            movie_detail_json[idx]['fields'].pop('production_companies')
            production_countries = movie_detail_json[idx]['fields'].pop('production_countries')
            if production_countries:
                movie_detail_json[idx]['fields']['country'] = production_countries[0]['name']
            movie_detail_json[idx]['fields'].pop('revenue')
            movie_detail_json[idx]['fields'].pop('spoken_languages')
            movie_detail_json[idx]['fields'].pop('status')
            movie_detail_json[idx]['fields'].pop('tagline')
            movie_detail_json[idx]['fields'].pop('video')

        with open("./whattowatch/api/fixtures/reform_movie_detail.json", "w", encoding="UTF-8") as outfile:
            json.dump(movie_detail_json, outfile, indent=4, ensure_ascii=False)

    # OTT 사이트 title을 TMDB data의 id로 변환
    def find_id(title):
        search_movie_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ko-KR&query={title}&page=1&include_adult=false'
        tmdb_data_res = requests.get(search_movie_url)
        tmdb_data_dict = json.loads(tmdb_data_res.content)
        movie_json = tmdb_data_dict['results'][0]

        return movie_json['id']

    # TMDB에 MOVIE데이터 요청
    def request_movie_data(id):
        movie_detail_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=ko-KR'
        tmdb_data_res = requests.get(movie_detail_url)
        tmdb_data_dict = json.loads(tmdb_data_res.content)
        return tmdb_data_dict

