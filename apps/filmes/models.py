from django.db import models
from django.urls import reverse

class Filmes(models.Model):
    
    title = models.CharField('Título', max_length=200)
    original_title = models.CharField('Título Original', max_length=200)
    image_url = models.URLField('Imagem')
    overview = models.TextField('Descrição')
    release_date = models.DateTimeField('Data de Lançamento', blank=True, null=True)
    vote_average = models.DecimalField('Avaliação', max_digits=5, decimal_places=2)
    adult = models.BooleanField('Filme Adulto', default='')
    original_language = models.CharField('Idioma Original', max_length=10)
    popularity = models.DecimalField('Popularidade', max_digits=10, decimal_places=5)
    vote_count = models.IntegerField('Quantidade de avaliações')
    to_watch = models.BooleanField('Filme na Watchlist?', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'