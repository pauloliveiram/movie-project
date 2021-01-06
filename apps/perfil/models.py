from django.db import models
from django.conf import settings

class Perfil(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='Perfil', on_delete=models.CASCADE, blank=True, null=True)
    #watchlist = models.ForeignKey(Watchlist, verbose_name='Watchlist', related_name='watchlist', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('Nome', max_length=100, null=True)

    def save_user(self, user):
        self.user = user
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
