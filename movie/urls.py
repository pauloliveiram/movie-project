"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from filmes import views as filmes_views
from usuarios import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', filmes_views.index, name='index'),
    path('entrar/', user_views.login_user, name='entrar'),
    path('logout/', user_views.logout_user, name='logout'),
    path('filme/<int:id>', filmes_views.single_movie, name='single_movie'),
    path('filme/update/<int:id>', filmes_views.update_watchlist, name='update_watchlist'),
    path('inicio/', filmes_views.user_inicio, name='user_inicio'),
]
