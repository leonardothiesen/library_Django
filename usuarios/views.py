from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
from library_ads.views import index

def login (request):
    status = request.GET.get('status')
    return render(request, 'pages/login.html', {'status':status})

def cadastro (request):
    status = request.GET.get('status')
    return render(request, 'pages/cadastro.html', {'status':status})


def valida_cadastro (request):
    nome_usuario = request.POST.get('nome_usuario')
    email_usuario = request.POST.get('email_usuario')
    senha_usuario = request.POST.get('senha_usuario')

    usuario = Usuario.objects.filter(email_usuario = email_usuario)

    if len(nome_usuario.strip()) == 0 or len(email_usuario.strip()) == 0:
        return redirect('/cadastro/?status=1')
    
    if len(senha_usuario) < 4:
        return redirect('/cadastro/?status=2')


    if len(usuario) > 0:
        return redirect('/cadastro/?status=3')
    
    try:
        senha_usuario = sha256(senha_usuario.encode()).hexdigest()
        usuario = Usuario(nome_usuario = nome_usuario,
                        email_usuario = email_usuario,
                        senha_usuario = senha_usuario)
        usuario.save()

        return redirect('/cadastro/?status=0')
    except:
        return redirect('/cadastro/?status=4')


def valida_login(request):
    email_usuario = request.POST.get('email_usuario')
    senha_usuario = request.POST.get('senha_usuario')
    senha_usuario = sha256(senha_usuario.encode()).hexdigest()
    
    usuario = Usuario.objects.filter(email_usuario = email_usuario).filter(senha_usuario = senha_usuario)

    if len (usuario) == 0:
        return redirect('/login/?status=1')

    request.session['usuario'] = usuario[0].id
    return index(request) 


def logout(request):
    request.session.flush()
    return redirect ('/login/')