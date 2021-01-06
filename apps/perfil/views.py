from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil
from .forms import PerfilForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from usuarios.models import User

@login_required
def criar_perfil(request):
    perfil_form = PerfilForm()
    perfil = Perfil.objects.filter(user=request.user)
    
    if perfil.count() < 4:
        if request.method == 'POST':
            perfil_form = PerfilForm(request.POST)

            if perfil_form.is_valid():
                perfil_form.instance.user = request.user
                perfil_form.save()
                return redirect('perfil:lista_perfis')
            else:
                return HttpResponse("Formulário Inválido")
    else:
        return HttpResponse('Já há o máximo de perfis cadastrados!')
        
    context = {'perfil_form': perfil_form}

    return render(request, 'criar_perfil.html', context)


@login_required
def atualizar_perfil(request, id):
    id = int(id)
    try:
        perfil = Perfil.objects.get(id=id)
    except Perfil.DoesNotExist:
        return redirect('perfil:criar_perfil')

    perfil_form = PerfilForm(request.POST or None, instance = perfil)
    if perfil_form.is_valid():
        perfil_form.save()
        return redirect('perfil:lista_perfis')

    context = {'perfil_form':perfil_form}

    return render(request, 'atualizar_perfil.html', context)

@login_required
def excluir_perfil(request, id):
    id = int(id)
    try:
        perfil = Perfil.objects.get(id=id)
    except Perfil.DoesNotExist:
        return redirect('perfil:lista_perfis')
    perfil.delete()
    return redirect('perfil:lista_perfis')

@login_required
def listar_perfis(request):
    perfil = Perfil.objects.filter(user=request.user)
    context = {'perfil': perfil}
    return render(request, 'lista_perfil.html', context)
