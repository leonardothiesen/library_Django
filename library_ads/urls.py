from django.urls import path
from . import views
from .views import book_detail

urlpatterns = [
    path('', views.index, name='home'),
    path('add-book/', views.add_book, name='add-book'),
    path('book-detail/<int:book_id>/', book_detail, name='book_detail')
]