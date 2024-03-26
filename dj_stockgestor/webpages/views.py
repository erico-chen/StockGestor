from django.http import HttpResponse
from django.shortcuts import render
from .models import Fornecedores


def home(request):
    return render(request, 'webpages/base_home.html')

def logado(request):
    if request.method == "POST":
        form = request.POST
        fornecedor = Fornecedores(nome_empresa=form["nome_empresa"], cnpj=form["cnpj"], inscricao_estadual=form["ie"]\
                                , inscricao_municipal=form["im"], endereco=form["endereco"], uf=form["uf"]\
                                , fornecedor_email=form["email"], fornecedor_telefone=form["telefone"])
        fornecedor.save()
       

    return render(request, 'webpages/base_logada.html')

