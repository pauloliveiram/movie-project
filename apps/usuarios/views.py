from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, CadastroForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@csrf_protect
def login_user(request):

    login_form = LoginForm()

    if request.user.is_authenticated:
        return redirect('user_inicio')

    else:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('entrar')

        else:
            login_form = LoginForm()

    context = {
        'login_form': login_form,
    }

    return render(request, 'login.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

def cadastro_user(request):
    if request.method == 'POST':
        cadastro_form = CadastroForm(request.POST)
        if cadastro_form.is_valid():
            user = cadastro_form.save()
            user = authenticate(
                username=user.username, password=cadastro_form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('entrar')
    else:
        cadastro_form = CadastroForm()
    context = {
        'cadastro_form': cadastro_form
    }
    return render(request, 'cadastro.html', context)