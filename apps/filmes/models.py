from django.db import models
from django.urls import reverse
from django.conf import settings

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

class Watchlist(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='Watchlist', on_delete=models.CASCADE)
    movie = models.ForeignKey(Filmes, verbose_name='Filme', related_name='Watchlist', on_delete=models.CASCADE)
    to_watch = models.BooleanField('Filme na Watchlist?', default=False)
    watched = models.BooleanField('Filme assistido?', default=False)

    def active_to_watch(self):
        self.to_watch = True
        self.save()

    def active_watched(self):
        self.watched = True
        self.save()

    class Meta:
        verbose_name = 'Watchlist'
        verbose_name_plural = 'Watchlist'
        unique_together = (('user', 'movie'),)
