# Generated by Django 3.1.4 on 2021-01-05 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_remove_perfil_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
    ]