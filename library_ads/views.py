from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from.models import Books, Genres
from random import randint
from usuarios.models import Usuario

def index (request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'pages/book_detail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre_id = request.POST.get('genre')
        genre_instance = Genres.objects.get(pk=genre_id)
        pages = request.POST.get('pages')
        cover = request.FILES.get('cover')
        author = request.POST.get('author')
        copies = request.POST.get('copies')
        cod = randint(100, 10000)

        Books.objects.create(
            name=name, genre=genre_instance, pages=pages, cover=cover,
            author=author, copies=copies, cod=cod 
        )

        return redirect('home')

    else:
        genres = Genres.objects.all()
        return render(request, 'pages/add-book.html', {'genres':genres})

def home_usuario(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome_usuario
        return HttpResponse(f'ola {usuario}')
    else:
        return redirect ('/login/?status=2')





# def search_book (request):
#     q = request.GET.get('q')
#     books = Books.objects.filter(name__icontains=q)
#     return render(request, 'pages/index.html', {'books':books})

# def delete_book(request, id):
#     book = Books.objects.get(id=id)
#     book.delete()
#     return redirect('home')

# def sell_book(request, id):
#     book = Books.objects.get(id=id)
#     book.qtd -= 1 
#     book.save()
#     return redirect('book-detail', id)