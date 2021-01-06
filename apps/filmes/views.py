from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Filmes, Watchlist
from .forms import WatchlistForm
from .utils import normalize
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from perfil.models import Perfil


@login_required
def user_inicio(request, id):
    filmes = Filmes.objects.all()
    perfil = Perfil.objects.get(id=id)
    watchlist = Watchlist.objects.filter(user=request.user, movie__in=filmes)

    busca = request.GET.get('search')
    if busca:
        query = normalize(busca)
        filmes = Filmes.objects.filter(title__icontains = query)

    context = {
        'filmes': filmes,
        'watchlist': watchlist,
        'perfil': perfil,
    }
    return render(request, 'user_inicio.html', context)


@login_required
def single_movie(request, id):
    filmes = Filmes.objects.get(id=id)
    movies_filter = Filmes.objects.filter(id=id)

    perfil = Perfil.objects.filter(user=request.user)
    watchlist = Watchlist.objects.filter(user=request.user, movie__in=movies_filter)

    context = {
        'filmes': filmes,
        'watchlist': watchlist,
    }
    return render(request, 'single_movie.html', context)

@login_required
def watchlist(request, id):
    movie = get_object_or_404(Filmes, id=id)
    watchlist, created = Watchlist.objects.get_or_create(
        user=request.user, movie=movie
    )
    if watched:
        watchlist.active_to_watch()


    return redirect('filme:single_movie', id)

@login_required
def excluir_watchlist(request, id):
    movie = get_object_or_404(Filmes, id=id)
    watched = Watchlist.objects.get(
        user=request.user, movie=movie
    )
    if watched:
        watched.deactivate_watched()

    return redirect('filme:single_movie', id)

@login_required
def watched(request, id):
    movie = get_object_or_404(Filmes, id=id)
    watched, created = Watchlist.objects.get_or_create(
        user=request.user, movie=movie
    )
    if watched:
        watched.active_watched()

    return redirect('filme:single_movie', id)