from django.contrib import admin
from .models import Filmes

class FilmesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Filmes, FilmesAdmin)