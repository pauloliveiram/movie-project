import os
import requests
from models import Filmes

url = 'https://api.themoviedb.org/3/movie/popular?api_key={0}&language=pt-br&page=1'.format(os.getenv('API_KEY'))
r = requests.get(url)
data = r.json()

for i in range(len(data['results'])):
    filme = Filmes(
        title = data['results'][i]['title'],
        image_url = 'https://image.tmdb.org/t/p/w500/' + data['results'][i]['poster_path'],
        overview = data['results'][i]['overview'],
        release_date = data['results'][i]['release_date'],
        vote_average = data['results'][i]['vote_average']
    )
    filme.save()