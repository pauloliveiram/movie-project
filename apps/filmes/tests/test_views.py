from django.test import TestCase
from django.test.client import Client 
from django.urls import reverse
from filmes.models import Filmes

class TestFilmesView(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_movies = 15

        for movie_id in range(number_of_movies):
            Filmes.objects.create(
                title = f'Wonder Woman 1984 {movie_id}',
                original_title = f'Wonder Woman 1984 {movie_id}',
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

    def test_status_code_index_by_url(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)

    def test_status_code_index_by_name(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
