from django import forms
from django.conf import settings
from .models import Watchlist

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['to_watch']