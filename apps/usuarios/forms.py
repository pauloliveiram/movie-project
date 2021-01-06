from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import User
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):

    username = forms.EmailField(label="", widget=forms.EmailInput(attrs={'type': 'text', 'placeholder': 'Nome de Usuário ou E-mail', 'required': 'required'}))
    password = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Senha','required': 'required'}))

class CadastroForm(forms.ModelForm):

    #username = forms.CharField(label='', widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username','required': 'required'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Senha','required': 'required'}))
    password2 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Confirmação de Senha','required': 'required'})
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe um usuário com esse e-mail')
        return email

    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date']
        labels = {
            'username': "",
            'first_name': "",
            'last_name': "",
            'email': "",
            'birth_date': "",
        }
        widgets = {
            'username': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username','required': 'required'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Nome','required': 'required'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Sobrenome','required': 'required'}),
            'email': forms.TextInput(attrs={'type': 'text', 'placeholder': 'E-mail','required': 'required'}),
            'birth_date': forms.DateTimeInput(attrs={'type':'datetime-local','placeholder': 'Data de Nascimento','required': 'required'}),
            }