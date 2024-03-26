from django.db import models
#IE IM ENDERECO UF EMAIL TELEFONE
class Fornecedores(models.Model):
    nome_empresa = models.CharField(max_length = 40)
    cnpj = models.CharField(max_length = 18)
    inscricao_estadual = models.CharField(max_length = 15)
    inscricao_municipal = models.CharField(max_length = 15)
    fornecedor_email = models.EmailField(max_length = 40)
    fornecedor_telefone = models.CharField(max_length = 12)