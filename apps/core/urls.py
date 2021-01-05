from django.urls import path, include
from . import views
from filmes.views import user_inicio

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', user_inicio, name='user_inicio'),
]