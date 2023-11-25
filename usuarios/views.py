from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect

def login (request):
    return render(request, 'pages/login.html')

def cadastro (request):
    return render(request, 'pages/cadastro.html')

def valida_cadastro (request):
    nome_usuario = request.POST.get('nome_usuario')
    email_usuario = request.POST.get('email_usuario')
    senha_usuario = request.POST.get('senha_usuario')

    usuario = Usuario.objects.filter(email_usuario = email_usuario)

    if len(nome_usuario.strip()) == 0 or len(email_usuario.strip()) == 0:
        return redirect('/login/?status=1')


    if len(usuario) > 0:
        return redirect('/login/?status=2')
    
    try:
        usuario = Usuario(nome_usuario = nome_usuario, email_usuario = email_usuario, senha_usuario = senha_usuario)
        usuario.save()

        return redirect('/login/?status=0')
    except:
        return redirect('/login/?status=3')





    return render(request, 'pages/valida_cadastro.html')
