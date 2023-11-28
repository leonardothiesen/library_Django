from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('book-detail/<int:book_id>/', views.book_detail , name='book-detail'),
    path('home-usuario/', views.home_usuario, name='home-usuario')
]