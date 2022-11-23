import json

with open("../api/fixtures/movie_details.json", "r", encoding="UTF-8") as f:
    movie_detail = json.load(f)

movie_title1 = []
movie_title2 = []

for i in range(len(movie_detail)//2):
    movie_title1.append(movie_detail[i]['fields']['title'])
for i in range(len(movie_detail)//2, len(movie_detail)):
    movie_title2.append(movie_detail[i]['fields']['title'])


with open("../api/fixtures/movie_title_1.json", "w", encoding="UTF-8") as f:
    json.dump(movie_title1, f, indent=4, ensure_ascii=False)

with open("../api/fixtures/movie_title_2.json", "w", encoding="UTF-8") as f:
    json.dump(movie_title2, f, indent=4, ensure_ascii=False)