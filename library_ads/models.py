from django.db import models
from datetime import datetime
from usuarios.models import Usuario

class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

from django.db import models
from datetime import datetime

class Books(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    pages = models.IntegerField()
    cover = models.ImageField(blank=True)
    author = models.CharField(max_length=255)
    cod = models.IntegerField(unique=True)
    date_register = models.DateTimeField(default=datetime.now)
    loan_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    borrowed = models.IntegerField(default=0)
    stock = models.IntegerField() 
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def borrow(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            self.borrowed += quantity
            self.save()


class Borrow(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.nome_usuario} emprestou {self.book.name}'
    

