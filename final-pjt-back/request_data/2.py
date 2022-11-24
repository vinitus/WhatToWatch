
import json
import requests
from tqdm import tqdm


with open("../api/fixtures/movie_ids.json", "r", encoding="UTF-8") as f:
    movie_ids = json.load(f)
    movie_set = set(movie_ids['movie_ids'])

with open("../api/fixtures/actor_new.json", "r", encoding="UTF-8") as f:
    actors = json.load(f)

with open("../api/fixtures/movie_ids_new.json", "r", encoding="UTF-8") as f:
    movie_new_ids = json.load(f)
    movie_new_set = set(movie_new_ids['movie_ids'])

with open("../api/fixtures/movie_detail_last.json", "r", encoding="UTF-8") as f:
    movie_details = json.load(f)
actor_movie_ids = []
for actor in actors:
    actor_movie_ids += actor['fields']['movies']
actor_movie_set = set(actor_movie_ids)



need_movie = list((movie_new_set - movie_set )|( actor_movie_set - movie_set))
except_ids = {'ids': []}
for movie_id in tqdm(need_movie):
    API = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=9186d5ace54e142f44d4f7e7a96d0043&language=ko-KR'
    movie_detail2 = requests.get(API)
    movie_detail = json.loads(movie_detail2.text)
    movie_data = {"model":"api.movie"}
    genres = []
    try:
        for genre in movie_detail['genres']:
            genres.append(genre['id'])
        movie_data["fields"] = {
            "adult": False,
            "belongs_to_collection": movie_detail['belongs_to_collection']['id'] if movie_detail.get('belongs_to_collection') else None,
            "id": movie_detail['id'],
            "original_language": movie_detail['original_language'],
            "overview": movie_detail['overview'],
            "popularity": movie_detail['popularity'],
            "poster_path": movie_detail["poster_path"],
            "release_date": movie_detail["release_date"],
            "runtime": movie_detail['runtime'],
            "title": movie_detail['title'],
            "vote_average": movie_detail['vote_average'],
            "vote_count": movie_detail['vote_count'],
            "genres": genres,
            "country": movie_detail['production_countries'][0]['name'] if movie_detail.get('production_countries') else None,
        }

    except:
        except_ids['ids'].append(movie_id)
    movie_details.append(movie_data)



datas = {'movie_ids': []}
datas['movie_ids'] = list((set(need_movie) | movie_set) - set(except_ids['ids']))

with open("../api/fixtures/movie_ids_new.json", "w", encoding="UTF-8") as f:
    json.dump(datas, f, indent=4, ensure_ascii=False)
with open("../api/fixtures/movie_details_last.json", "w", encoding="UTF-8") as f:
    json.dump(movie_details, f, indent=4, ensure_ascii=False)
with open("../api/fixtures/except_ids.json", "w", encoding="UTF-8") as f:
    json.dump(except_ids, f, indent=4, ensure_ascii=False)
