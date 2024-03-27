from django.shortcuts import render
from .models import Produto

def cad_produto(request):
    return render(request,'produtos/cadastro_produto.html')

def produtos(request):
    novo_produto = Produto()
    novo_produto.cod = request.POST.get('cod')
    novo_produto.produto = request.POST.get('produto')
    novo_produto.bar_cod = request.POST.get('bar_cod')
    novo_produto.ref = request.POST.get('ref')
    novo_produto.marca = request.POST.get('marca')
    novo_produto.categoria = request.POST.get('categoria')
    novo_produto.qtd = request.POST.get('qtd')
    novo_produto.preco_compra = request.POST.get('preco_compra')
    novo_produto.local = request.POST.get('local')
    novo_produto.entrada = request.POST.get('entrada')
    novo_produto.validade = request.POST.get('validade')
    novo_produto.estoque = request.POST.get('estoque')
    novo_produto.save()

    produtos = {
        'produtos': Produto.objects.all()
    }

    return render(request,'produtos/listagem_estoque.html',produtos)
    
    
    
