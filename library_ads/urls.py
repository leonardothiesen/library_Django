from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='home'),
    path('book-detail/<int:id>/', views.book_detail , name='book-detail'),
]