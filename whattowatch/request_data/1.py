import requests
import json
from tqdm import tqdm
TMDB_API_KEY = '9186d5ace54e142f44d4f7e7a96d0043'



with open("../api/fixtures/actor.json", "r", encoding="UTF-8") as f:
    actors = json.load(f)
with open("../api/fixtures/director.json", "r", encoding="UTF-8") as f:
    directors = json.load(f)
with open("../api/fixtures/movie_ids.json", "r", encoding="UTF-8") as f:
    movie_ids = json.load(f)
    movie_set = set(movie_ids['movie_ids'])
with open("../api/fixtures/movie_detail.json", "r", encoding="UTF-8") as f:
    movie_details = json.load(f)

act_direct_movie_ids = []
for actor in actors:
    act_direct_movie_ids += actor['fields']['movies']
for director in directors:
    act_direct_movie_ids += director['fields']['movies']

need_movie_ids = list(set(act_direct_movie_ids) - movie_set)

for movie_id in tqdm(need_movie_ids):
    MOVIE_DETAIL_API_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR'
    movie_detail = requests.get(MOVIE_DETAIL_API_URL)
    movie_detail_json = json.loads(movie_detail.text)
    
    movie_detail_dict = {"model": "api.movie"}
    genre_lst = []
    try:
        for mv_genre in movie_detail_json['genres']:
            genre_lst.append(mv_genre['id'])
        
        country = movie_detail_json['production_countries'][0]['name'] if movie_detail_json['production_countries'] else None
        movie_detail_dict['fields'] = {
            "adult": False,
            "belongs_to_collection": movie_detail_json['belongs_to_collection']['id'] if movie_detail_json['belongs_to_collection'] else None,
            "id": movie_detail_json['id'],
            "original_language": movie_detail_json['original_language'],
            "overview": movie_detail_json['overview'],
            "popularity": movie_detail_json["popularity"],
            "poster_path": movie_detail_json["poster_path"],
            "release_date": movie_detail_json["release_date"],
            "runtime": movie_detail_json[ "runtime"],
            "title": movie_detail_json["title"],
            "vote_average": movie_detail_json["vote_average"],
            "vote_count": movie_detail_json["vote_count"],
            "genres": genre_lst,
            "country": country
        }
        movie_details.append(movie_detail_dict)
    except:
        continue

movie_ids['movie_id'] += need_movie_ids


with open("../api/fixtures/movie_ids_new.json", "w", encoding="UTF-8") as f:
    json.dump(movie_ids, f, indent=4, ensure_ascii=False)

with open("../api/fixtures/movie_detail_new.json", "w", encoding="UTF-8") as f:
    json.dump(movie_details, f, indent=4, ensure_ascii=False)