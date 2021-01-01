import os
import requests

#Função para importar os dados sobre filmes populares da API do TMDB
def get_results():
    results_list = []
    url = 'https://api.themoviedb.org/3/movie/popular?api_key={0}&language=pt-br&page=1'.format(os.getenv('API_KEY'))
    r = requests.get(url)
    data = r.json()

    for i in range(len(data['results'])):
        data['results'][i]['image_url'] = 'https://image.tmdb.org/t/p/w500/' + data['results'][i]['poster_path']
        results_list.append(data['results'][i])
    return results_list
