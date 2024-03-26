from django.db import models

class Fornecedores(models.Model):
    nome_empresa = models.CharField(max_length = 40)
    cnpj = models.CharField(max_length = 18)
    inscricao_estadual = models.CharField(max_length = 15)
    inscricao_municipal = models.CharField(max_length = 15)
    endereco = models.CharField(max_length = 40, default="NULL")
    uf = models.CharField(max_length = 2, default="NULL")
    fornecedor_email = models.EmailField(max_length = 40)
    fornecedor_telefone = models.CharField(max_length = 12)