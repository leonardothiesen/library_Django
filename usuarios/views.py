from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def login (request):
    return render(request, 'pages/login.html')

def cadastro (request):
    return render(request, 'pages/cadastro.html')

def valida_cadastro (request):
    nome_usuario = request.POST.get('nome_usuario')
    email_usuario = request.POST.get('email_usuario')
    senha_usuario = request.POST.get('senha_usuario')
    return HttpResponse (f"{nome_usuario} {email_usuario} {senha_usuario}")
