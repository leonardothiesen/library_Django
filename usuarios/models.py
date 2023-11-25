from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField()
    senha_usuario = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome_usuario


    
