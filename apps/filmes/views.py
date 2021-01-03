from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Filmes

'''class GetResults(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        results = get_results()
        if request.GET.get('to_watch_movie'):
            results['count']['to_watch'] = True
            print('Esta true')        
        context = {
            'results': results,
        }
        return context   '''     

def index(request):
    filmes = Filmes.objects.all()
    context = {
        'filmes': filmes
    }
    return render(request, 'index.html', context)