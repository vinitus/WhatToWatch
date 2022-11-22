import json
import requests
from time import sleep
from .secret import TMDB_API_KEY
from tqdm import tqdm
import os



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
        with open("./whattowatch/api/fixtures/raw_movie_list.json", "w", encoding="UTF-8") as outfile:
            json.dump(movie_list_json, outfile, indent=4, ensure_ascii=False)


    # 저장해둔 raw_movie_list.json에서 id를 읽어와 detail 요청을 보내기
    def load_movie_detail(self):
        with open("./whattowatch/api/fixtures/raw_movie_list.json", "r", encoding="UTF-8") as f:
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

        with open("./whattowatch/api/fixtures/raw_movie_detail.json", "w", encoding="UTF-8") as outfile:
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
        with open("./whattowatch/api/fixtures/raw_movie_list.json", "r", encoding="UTF-8") as f:
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

        with open("./whattowatch/api/fixtures/raw_credit.json", "w", encoding="UTF-8") as outfile:
            json.dump(credit_json, outfile, indent=4, ensure_ascii=False)

    # TMDB movie detail response 형식 바꾸기
    def transform_movie_detail_json(self):
        with open("./whattowatch/api/fixtures/raw_movie_detail.json", "r", encoding="UTF-8") as f:
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

        with open("./whattowatch/api/fixtures/movie_detail.json", "w", encoding="UTF-8") as outfile:
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

    def transform_credit(self):
        with open("./whattowatch/api/fixtures/raw_credit.json", "r", encoding="UTF-8") as f:
            credit_json = json.load(f)
        
        actor_json = []
        director_json = []
        for credit in credit_json:
            movie_id = credit['id']

            actor_list = credit['cast'][:9]
            for actor in actor_list:
                actor_dict = {
                    'model': 'api.actor',
                    'fields': {
                        'id': actor['id'],  
                        'movies': movie_id,
                        'name': actor['name']
                    }
                }
                actor_json.append(actor_dict)

            crew_list = credit['crew']
            for crew in crew_list:
                if crew['job'] == 'Director':
                    director_dict = {
                        'model': 'api.director',
                        'fields': {
                            'id': crew['id'],
                            'movies': movie_id,
                            'name': crew['name']
                        }
                    }
                    break
            director_json.append(director_dict)

        with open("./whattowatch/api/fixtures/actor.json", "w", encoding="UTF-8") as f:
            json.dump(actor_json, f, indent=4, ensure_ascii=False)

        with open("./whattowatch/api/fixtures/director.json", "w", encoding="UTF-8") as f:
            json.dump(director_json, f, indent=4, ensure_ascii=False)

    def movie_ids_to_json(self):
        with open("./whattowatch/api/fixtures/movie_detail.json", "r", encoding="UTF-8") as f:
            movie_json = json.load(f)
        
        movie_ids = []
        for movie in movie_json:
            movie_ids.append(movie['fields']['id'])
        data = {
            'movie_ids': movie_ids
        }
        with open("./whattowatch/api/fixtures/movie_ids.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def movie_titles_to_json(self):
        with open("./whattowatch/api/fixtures/movie_detail.json", "r", encoding="UTF-8") as f:
            movie_json = json.load(f)

        with open("./whattowatch/api/fixtures/actor_based_movies.json", "r", encoding="UTF-8") as f:
            more_movie_json = json.load(f)
        
        movie_titles = []
        for movie in movie_json:
            movie_titles.append(movie['fields']['title'])
        for movie in more_movie_json:
            movie_titles.append(movie['fields']['title'])
        data = {
            'movie_titles': movie_titles
        }
        with open("./whattowatch/api/fixtures/movie_titles.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def actor_conect_movie(self):
        with open("./whattowatch/api/fixtures/movie_ids.json", "r", encoding="UTF-8") as f:
            db_movie_ids = json.load(f)
        db_movie_ids = set(db_movie_ids['movie_ids'])
        movie_ids = set()
        data_actor_movie = []
        movie_datas = []
        need_add_ids = set()
        with open("./whattowatch/api/fixtures/actor.json", "r", encoding="UTF-8") as f:
            actor_json = json.load(f)
        for actor in tqdm(actor_json):
            actor_movies = []
            actor_id = actor['fields']['id']
            ACTOR_DETAIL_API = f'https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={TMDB_API_KEY}&language=ko-KR'
            actor_res = requests.get(ACTOR_DETAIL_API)
            actor_res = json.loads(actor_res.text)
            for act in actor_res['cast']:
                actor_movies.append(act['id'])

                if not db_movie_ids.intersection({act['id']}) and not need_add_ids.intersection({act['id']}):
                    need_add_ids.add(act['id'])
                    movie_detail_url = f'https://api.themoviedb.org/3/movie/{act["id"]}?api_key={TMDB_API_KEY}&language=ko-KR'
                    tmdb_data_res = requests.get(movie_detail_url)
                    tmdb_data_dict = json.loads(tmdb_data_res.content)
                    movie_genres = []
                    for genre in tmdb_data_dict['genres']:
                        movie_genres.append(genre['id'])
                
                    movie_data = {"model": "api.movie"}
                    fields = {}
                    fields['adult'] = tmdb_data_dict['adult']
                    if tmdb_data_dict.get('belongs_to_collection'):
                        fields['belongs_to_collection'] = tmdb_data_dict['belongs_to_collection']['id']
                    fields['id'] = tmdb_data_dict['id']
                    fields['backdrop_path'] = tmdb_data_dict['backdrop_path']
                    fields['original_language'] = tmdb_data_dict['original_language']
                    fields['overview'] = tmdb_data_dict['overview']
                    fields['popularity'] = tmdb_data_dict['popularity']
                    fields['poster_path'] = tmdb_data_dict['poster_path']
                    fields['release_date'] = tmdb_data_dict['release_date']
                    fields['runtime'] = tmdb_data_dict['runtime']
                    fields['title'] = tmdb_data_dict['title']
                    fields['vote_average'] = tmdb_data_dict['vote_average']
                    fields['vote_count'] = tmdb_data_dict['vote_count']
                    fields['genres'] = movie_genres
                    if tmdb_data_dict['production_countries']:
                        fields['country'] = tmdb_data_dict['production_countries'][0]['name']
                    movie_data['fields'] = fields
                    movie_datas.append(movie_data)

            data_actor_movie.append({
                'model': "api.actor",
                'fields': {
                    "id":actor_id,
                    "movies": actor_movies,
                    "name": actor['fields']['name']
                }
            })
        with open("./whattowatch/api/fixtures/movie_ids.json", "r", encoding="UTF-8") as f:
            movie_ids_json = json.load(f)
            new_ids = movie_ids_json['movie_ids'] + list(need_add_ids)
        new_movie_ids = {
            'movie_ids':new_ids
        }
        with open("./whattowatch/api/fixtures/movie_ids.json", "w", encoding="UTF-8") as f:
            json.dump(new_movie_ids, f, indent=4, ensure_ascii=False)
        with open("./whattowatch/api/fixtures/actor.json", "w", encoding="UTF-8") as f:
            json.dump(data_actor_movie, f, indent=4, ensure_ascii=False)
        with open("./whattowatch/api/fixtures/actor_based_movies.json", "w", encoding="UTF-8") as f:
            json.dump(movie_datas, f, indent=4, ensure_ascii=False)