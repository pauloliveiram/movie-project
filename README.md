<h2> Aplicação Web em Django para gerenciamento de filmes

<h3> Instruções para rodar o projeto
 
 Para rodar o projeto, é necessário ter o Python e o gerenciador de pacoter Pip instalados no computador. Após clonar o repositório, é necessário criar um ambiente virtual para o gerenciamento das dependências do projeto
 <p> Então, para instalar o ambiente virtual, execute: 
 
					    	python -m venv nome_do_ambiente_virtual
	
<p> Para ativar o ambiente virtual:

					  (Windows) nome_do_ambiente_virtual\Scripts\activate
					  (Linux) source nome_do_ambiente_virtual\bin\activate
					
<p> Após ativar o ambiente, é necessário instalar as dependências. Portanto execute:
	
					    	   pip install -r requirements.txt
								
<p> Agora, é necessário rodar as migrações no banco de dados. Portanto, execute:
	
						  	python manage.py migrate
							
<p> Por fim, rode o servidor com o seguinte comando:
	
						        python manage.py runserver
