from django import forms
from django.conf import settings
from .models import Filmes

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = ['to_watch']