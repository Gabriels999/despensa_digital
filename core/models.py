from django.db import models

# Create your models here.

class Marca(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=128)
    peso = models.FloatField()
    preco = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="marca")
    tipo = models.CharField(max_length=64, default='Cozinha')
    em_estoque = models.IntegerField(default=0)
    necessario = models.IntegerField(default=1)

    def __str__(self):
        if self.tipo == 'Cozinha':
            return f"{self.nome} | {self.marca} - {self.peso}Kg: R$ {self.preco}"
        else:
            return f"{self.nome} | {self.marca} - {self.peso} uni: R$ {self.preco}"

    def precisa_comprar(self):
        if self.em_estoque < self.necessario:
            return True
        else:
            return False