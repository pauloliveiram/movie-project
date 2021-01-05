from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome de Usuário', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('Nome', max_length=100, blank=True)
    last_name = models.CharField('Nome', max_length=100, blank=True)
    birth_date = models.DateTimeField('Data de Nascimento', null=True)
    is_staff = models.BooleanField('Membro da equipe', default=False)
    is_superuser = models.BooleanField('Admin do sistema', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.first_name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
