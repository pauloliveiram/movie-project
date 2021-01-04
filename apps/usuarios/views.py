from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
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
                return redirect('user_inicio')

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