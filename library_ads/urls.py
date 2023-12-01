from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('book-detail/<int:id>/', views.book_detail, name='book_detail'),
    path('search-book/', views.search_book, name='search-book'),
    path('home-usuario/', views.home_usuario, name='home-usuario'),
    path('burrow-book/<int:id>/', views.burrow_book, name='burrow-book'),
    path('return-book/<int:id>/', views.return_book, name='return-book'),
]
