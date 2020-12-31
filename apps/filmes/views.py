from django.shortcuts import render
from django.views.generic import TemplateView
from .api import get_results

class GetResults(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'results': get_results(),
        }
        return context