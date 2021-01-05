from django.urls import path, include
from . import views

urlpatterns = [
    path('entrar/', views.login_user, name='entrar'),
    path('logout/', views.logout_user, name='logout'),
    path('cadastro/', views.cadastro_user, name='cadastro'),
]