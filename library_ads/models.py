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

class Books(models.Model):
    
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE) 
    pages = models.IntegerField()
    cover = models.ImageField(blank=True)
    author = models.CharField(max_length=255)
    copies = models.IntegerField()
    cod = models.AutoField(primary_key=True)
    date_register = models.DateTimeField(default=datetime.now)
    borrowed = models.BooleanField(default=False)
    loan_date = models.DateTimeField(blank=True, null=True) 
    return_date = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
