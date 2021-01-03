from django.test import TestCase
from filmes.models import Filmes

class FilmeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Filmes.objects.create(
            title = 'Wonder Woman 1984',
            original_title = 'Wonder Woman 1984',
            image_url = 'https://image.tmdb.org/t/p/w500/8UlWHLMpgZm9bx6QYh0NFoq67TZ.jpg',
            overview = 'Wonder Woman comes into conflict with the Soviet Union during the Cold War in the 1980s and finds a formidable foe by the name of the Cheetah.',
            release_date = '2020-12-16',
            vote_average = 7.3,
            adult = False,
            original_language = 'en-us',
            popularity = 7842.973,
            vote_count = 1879,
            to_watch = False,
        )

#Funções para testar as labels de cada campo do model Filmes
    def test_title_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Título')

    def test_original_title_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('original_title').verbose_name
        self.assertEquals(field_label, 'Título Original')

    def test_image_url_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('image_url').verbose_name
        self.assertEquals(field_label, 'Imagem')

    def test_overview_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('overview').verbose_name
        self.assertEquals(field_label, 'Descrição')

    def test_release_date_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('release_date').verbose_name
        self.assertEquals(field_label, 'Data de Lançamento')

    def test_vote_average_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('vote_average').verbose_name
        self.assertEquals(field_label, 'Avaliação')

    def test_adult_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('adult').verbose_name
        self.assertEquals(field_label, 'Filme Adulto')

    def test_original_language_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('original_language').verbose_name
        self.assertEquals(field_label, 'Idioma Original')

    def test_popularity_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('popularity').verbose_name
        self.assertEquals(field_label, 'Popularidade')

    def test_vote_count_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('vote_count').verbose_name
        self.assertEquals(field_label, 'Quantidade de avaliações')

    def test_to_watch_label(self):
        filme = Filmes.objects.get(id=1)
        field_label = filme._meta.get_field('to_watch').verbose_name
        self.assertEquals(field_label, 'Filme na Watchlist?')

#Fim dos testes de labels

#Teste do atributo max_length nos campos title e original_title
    def test_title_max_length(self):
        filme = Filmes.objects.get(id=1)
        max_length = filme._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_original_title_max_length(self):
        filme = Filmes.objects.get(id=1)
        max_length = filme._meta.get_field('original_title').max_length
        self.assertEquals(max_length, 200)

#Teste do atributo max_digits no campo vote_average
    def test_vote_average_max_digits(self):
        filme = Filmes.objects.get(id=1)
        max_digits = filme._meta.get_field('vote_average').max_digits
        self.assertEquals(max_digits, 5)

#Teste do atributo decimal_places no campo vote_average
    def test_vote_average_digital_places(self):
        filme = Filmes.objects.get(id=1)
        decimal_places = filme._meta.get_field('vote_average').decimal_places
        self.assertEquals(decimal_places, 2)

#Teste da função __str__() no model Filmes
    def test_object_name(self):
        filme = Filmes.objects.get(id=1)
        expected_object_name = f'{filme.title}'
        self.assertEquals(expected_object_name, str(filme))
