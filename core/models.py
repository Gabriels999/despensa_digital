from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=128)
    peso = models.IntegerField()
    preco = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="marca")
    tipo = models.CharField(max_length=64, default='Cozinha')

    def __str__(self):
        if self.tipo == 'Cozinha':
            return f"{self.nome} | {self.marca} - {self.peso}Kg: R$ {self.preco}"
        else:
            return f"{self.nome} | {self.marca} - {self.peso} uni: R$ {self.preco}"