from django.shortcuts import render, HttpResponse, redirect
from.models import Books, Genres
from random import randint
from usuarios.models import Usuario
from .forms import BorrowBookForm, ReturnBookForm


def index (request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books': books})

def book_detail(request, id):
    print(f"{id}")
    book = Books.objects.get(id=id)
    return render(request, 'pages/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre_id = request.POST.get('genre')
        genre_instance = Genres.objects.get(pk=genre_id)
        pages = request.POST.get('pages')
        cover = request.FILES.get('cover')
        author = request.POST.get('author')
        stock = request.POST.get('stock')
        cod = randint(100, 10000) 

        Books.objects.create(
            name=name, genre=genre_instance, pages=pages, cover=cover,
            author=author, stock=stock, cod=cod 
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

def search_book (request):
    q = request.GET.get('q')
    books = Books.objects.filter(name__icontains=q)
    return render(request, 'pages/index.html', {'books':books})


def burrow_book(request, id):
    book = Books.objects.get(id=id)

    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrow_quantity = form.cleaned_data['borrow_quantity']

            if 1 <= borrow_quantity <= book.stock:
                book.stock -= borrow_quantity
                book.borrowed += borrow_quantity
                book.save()

                return redirect('home')

    else:
        form = BorrowBookForm()

    return redirect('home')

def return_book(request, id):
    book = Books.objects.get(id=id)

    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            return_quantity = form.cleaned_data['return_quantity']

            if 1 <= return_quantity <= book.borrowed:
                book.stock += return_quantity
                book.borrowed -= return_quantity
                book.save()

                return redirect('home')

    else:
        form = ReturnBookForm()

    return redirect('home')






# def burrow_book(request, id):
#     book = Books.objects.get(id=id)
#     book.burrow()
#     return redirect('home')

# def loan_book(request, id):
#     book = Books.objects.get(id=id)
#     book.qtd -= 1 
#     book.save()
#     return redirect('book-detail', id)