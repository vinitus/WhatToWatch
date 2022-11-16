import json
import requests
from secret import TMDB_API_KEY



def find_id(title):
    search_movie_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ko-KR&query={title}&page=1&include_adult=false'
    tmdb_data_res = requests.get(search_movie_url)
    tmdb_data_dict = json.loads(tmdb_data_res.content)
    movie_json = tmdb_data_dict['results'][0]
    return movie_json.id


        

