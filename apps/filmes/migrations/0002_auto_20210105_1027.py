# Generated by Django 3.1.4 on 2021-01-05 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Watchlist', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('user', 'movie')},
        ),
    ]
