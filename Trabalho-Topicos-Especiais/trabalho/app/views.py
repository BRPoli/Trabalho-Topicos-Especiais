from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarefas

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method  == 'GET':
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Usuario ja registrado!')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse(render(request, 'login.html'))


    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)
        if user:
            login_django(request,user)
            return HttpResponse(render(request, 'agenda.html'))
        else:
            return HttpResponse('Usuario ou senha invalida! Tente Novamente!')
    
def agenda(request):
    if request.method == 'GET':
        listar = {
            'lista': Tarefas.objects.all()
        }
        return render(request, 'agenda.html', listar)
    else:
        return render(request, 'adicionaTarefa.html')
    
def addTarefa(request):
    if request.method == 'GET':
        return render(request, 'adicionaTarefa.html')
    else: 
        nova_tarefa = Tarefas()
        nova_tarefa.titulo = request.POST.get('titulo')
        nova_tarefa.descricao = request.POST.get('descricao')
        nova_tarefa.data_criacao = request.POST.get('data')
        nova_tarefa.status = request.POST.get('status')
        nova_tarefa.save()
        listar = {
            'lista': Tarefas.objects.all()
        }
        return render(request, 'agenda.html', listar)