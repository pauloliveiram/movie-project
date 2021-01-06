from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'filme'

urlpatterns = [
    path('<int:id>', views.single_movie, name='single_movie'),
    path('update-watchlist/<int:id>', views.watchlist, name='update_watchlist'),
    path('excluir-watchlist/<int:id>', views.excluir_watchlist, name='excluir_watchlist'),
    path('watched/<int:id>', views.watched, name='watched'),
]