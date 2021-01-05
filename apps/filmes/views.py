from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Filmes
from .forms import WatchlistForm
from .utils import normalize
from django.contrib.auth.decorators import login_required


@login_required
def user_inicio(request):
    filmes = Filmes.objects.all()
    busca = request.GET.get('search')
    if busca:
        query = normalize(busca)
        filmes = Filmes.objects.filter(title__icontains = query)
    context = {
        'filmes': filmes,
    }
    return render(request, 'user_inicio.html', context)

@login_required
def single_movie(request, id):
    filmes = Filmes.objects.get(id=id)
    context = {
        'filmes': filmes,
    }
    return render(request, 'single_movie.html', context)

@login_required
def update_watchlist(request, id):
    try:
        filme = Filmes.objects.get(id=id)
    except Filmes.DoesNotExist:
        return redirect('index')

    filme_form = WatchlistForm(request.POST or None, instance=filme)
    if filme_form.is_valid():
        filme_form.save()
        return redirect('index')
    
    context = {
        'filme_form': filme_form,
        'filme':filme,
    }
    return render(request, 'update_watchlist.html', context)