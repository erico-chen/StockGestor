from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    cod = models.IntegerField()
    estoque = models.IntegerField()
    bar_cod = models.IntegerField()
    qtd = models.IntegerField()
    preco_compra = models.FloatField()
    produto = models.TextField()
    ref = models.TextField()
    marca = models.TextField()
    categoria = models.TextField()
    local = models.TextField()
    fornecedor = models.TextField()
    entrada = models.DateField()
    validade = models.DateField()
