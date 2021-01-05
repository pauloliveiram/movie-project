from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Filmes, Watchlist
from .forms import WatchlistForm
from .utils import normalize
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def user_inicio(request):
    filmes = Filmes.objects.all()
    watchlist = Watchlist.objects.filter(user=request.user, movie__in=filmes)

    busca = request.GET.get('search')
    if busca:
        query = normalize(busca)
        filmes = Filmes.objects.filter(title__icontains = query)

    context = {
        'filmes': filmes,
        'watchlist': watchlist,
    }
    return render(request, 'user_inicio.html', context)

@login_required
def single_movie(request, id):
    filmes = Filmes.objects.get(id=id)
    movies_filter = Filmes.objects.filter(id=id)
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
    if created:
        watchlist.active_to_watch()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')

    return redirect('single_movie')

@login_required
def watched(request, id):
    movie = get_object_or_404(Filmes, id=id)
    watched, created = Watchlist.objects.get_or_create(
        user=request.user, movie=movie
    )
    if created:
        watched.active_watched()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')

    return redirect('single_movie')