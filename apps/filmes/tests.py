from django.test import TestCase
from django.test.client import Client 
from django.urls import reverse

class TestFilmesView(TestCase):

    def test_status_code(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')