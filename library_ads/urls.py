from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('book-detail/<int:id>/', views.book_detail , name='book-detail'),
    path('search-book/', views.search_book, name='search-book'),
    path('home-usuario/', views.home_usuario, name='home-usuario')
]