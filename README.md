# Movie Project
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/pauloliveiram/movie-project/blob/main/LICENSE)

## Sobre o projeto

[http://pauloliveiram.pythonanywhere.com/](http://pauloliveiram.pythonanywhere.com/)

O Movie Project é uma aplicação fullstack web que consiste em uma plataforma para gerenciamento de filmes, em que o usuário dispõe de uma lista de filmes, podendo gerar uma watchlist, uma lista com os filmes que deseja assistir. 

## Layout web


![2022-12-22-17-05-pauloliveiram.pythonanywhere.com.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de466edb-3ed2-4ddb-a47d-058d5f2cd2eb/2022-12-22-17-05-pauloliveiram.pythonanywhere.com.png)

## Tecnologias utilizadas

### Back-end

- Python
- Django

### Front-end

- HTML
- CSS
- JavaScript

### Implantação em produção

- Front-end e back-end: Pythonanywhere
- Banco de dados: SQLite

## Integrações

### API TMDB

Foi consumida a API disponibilizada pela TMDB para o fornecimento das informações dos filmes

## Features

- Criação de conta: Permite o usuário a realizar o cadastro de uma conta
- Login: O usuário pode realizar o login na plataforma através das informações fornecidas no cadastro
- Criação de Perfil: Criar um perfil para a utilização de um usuário. Podem ser cadastrados até 4 perfis por conta.
- Adicionar filme na Watchlist: O usuário pode ver as informações de cada filme e adicioná-lo na sua Watchlist


## Como executar o projeto

### Pré-requisitos

- Python ≥ 7.0
- Pip


```bash

# Clonar repositório
git clone https://github.com/pauloliveiram/movie-project.git

# Entrar na pasta do projeto
cd movie-project

# Criar um ambiente virtual 
python -m venv venv
	
# Ativar o ambiente virtual

(Windows) venv\Scripts\activate
(Linux) source venv/bin/activate
					
# Instalar as dependências do projeto
pip install -r requirements.txt
								
# Executar as migrações no banco de dados
python manage.py migrate
							
# Executar o servidor
python manage.py runserver
```							

# Autor

Paulo Oliveira

[https://www.linkedin.com/in/pauloliveiram/](https://www.linkedin.com/in/pauloliveiram/)


