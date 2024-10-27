from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    if request.method == 'POST':
        # Populando a variável formulario com os dados inputados pelo usuário
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            # Salvar usuário no banco de dados
            formulario.save()
            # Informar ao usuário
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
        
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', context={'formulario': formulario})