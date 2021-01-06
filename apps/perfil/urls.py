from django.urls import path, include
from . import views

app_name = 'perfil'

urlpatterns = [
    path('criar-perfil/', views.criar_perfil, name='criar_perfil'),
    path('atualizar-perfil/<int:id>', views.atualizar_perfil, name='atualizar_perfil'),
    path('lista-perfis/', views.listar_perfis, name='lista_perfis'),
    path('excluir-perfil/<int:id>/', views.excluir_perfil, name='excluir_perfil'),
]