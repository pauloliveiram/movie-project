from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):

    username = UsernameField(label="", widget=forms.TextInput(attrs={
        'type': 'text', 
        'placeholder': 'Username',
        'required': 'required'}))
    password = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'type': 'password', 
            'placeholder': 'Senha',
            'required': 'required'
        }),
    )