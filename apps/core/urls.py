from django.urls import path, include
from . import views
from filmes.views import user_inicio

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:id>', user_inicio, name='user_inicio'),
]