# Generated by Django 3.1.4 on 2021-01-05 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0004_merge_20210105_1028'),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='movie',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='watchlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='filmes.filmes', verbose_name='Watchlist'),
        ),
    ]
