from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.single_movie, name='single_movie'),
    path('update/<int:id>', views.watchlist, name='update_watchlist'),
    path('watched/<int:id>', views.watched, name='watched'),
]