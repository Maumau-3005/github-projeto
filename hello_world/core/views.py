from django.shortcuts import render, redirect
from .models import Inscricao
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, "index.html")

def calendario(request):
    return render(request, 'calendario.html')

def faq(request):
    return render(request, 'faq.html')
    
@login_required  # Garante que apenas usuários logados possam acessar
def inscrever_se(request):
    if request.method == 'POST':
        tipo_musica = request.POST['tipo_musica']
        horario_disponivel = request.POST['horario_disponivel']
        descricao_show = request.POST['descricao_show']

        # Verificar se o horário já está ocupado
        if Inscricao.objects.filter(horario_disponivel=horario_disponivel).exists():
            messages.error(request, 'Esse horário já está ocupado. Escolha outro.')
        else:
            Inscricao.objects.create(
                usuario=request.user,
                tipo_musica=tipo_musica,
                horario_disponivel=horario_disponivel,
                descricao_show=descricao_show
            )
            messages.success(request, 'Inscrição realizada com sucesso!')
            return redirect('index')

    return render(request, 'inscrever_se.html')

@login_required
def inscrever_se(request):
    return render(request, 'inscrever_se.html')

def login_usuario(request):
    formulario = AuthenticationForm()  # Formulário padrão do Django
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()  # Obtém o usuário autenticado
            login(request, usuario)  # Autentica o usuário
            return redirect('index')  # Redireciona após login
    return render(request, 'iniciar_sessao.html', {'formulario': formulario})

def logout_usuario(request):
    logout(request)
    return redirect('iniciar_sessao')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Agora você pode fazer login.')
            return redirect('iniciar_sessao')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})