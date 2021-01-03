import os
import requests

#Função para importar os dados sobre filmes populares da API do TMDB
def get_results():

    #Requisição dos dados da API
    url = 'https://api.themoviedb.org/3/movie/popular?api_key={0}&language=pt-br&page=1'.format(os.getenv('API_KEY'))
    r = requests.get(url)
    data = r.json()

    #Adicionando os dados sobre os filmes em uma lista
    results_list = []
    for i in range(len(data['results'])):
        data['results'][i]['image_url'] = 'https://image.tmdb.org/t/p/w500/' + data['results'][i]['poster_path'] #Criação de uma variável para armazenar a URL completa da imagem do cartaz
        data['results'][i]['to_watch'] = False #Criação de uma variável booleana responsável por informar se o filme está na lista "Para Assistir"
        data['results'][i]['count'] = i
        results_list.append(data['results'][i])  
    return results_list
