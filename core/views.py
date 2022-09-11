from multiprocessing import context
from django.shortcuts import render, redirect

from core.models import Produto, Marca
from core.forms import ProdutoForm, MarcaForm

# Create your views here.

# Read Data
def lista_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    context = {
        'produtos': produtos
    }
    return render(request, "core/lista_produtos.html", context)

def lista_de_compras(request):
    produtos = Produto.objects.all().order_by('nome')
    lista_de_compras = []
    for item in produtos:
        print(item.precisa_comprar())
        if item.precisa_comprar() == True:
            lista_de_compras.append(item)
            context = {
                'produtos': lista_de_compras
            }
    if len(lista_de_compras) == 0:
        return render(request, "core/nenhuma_compra.html")
    else:
        return render(request, "core/lista_produtos.html", context)

def lista_marcas(request):
    marcas = Marca.objects.all().order_by('nome')
    context = {
        'marcas': marcas
    }
    return render(request, 'core/lista_marcas.html', context)

def lista_produtos_marca(request, id):
    produtos = Produto.objects.filter(marca=id)
    context = {
        "produtos": produtos
    }
    return render(request, "core/lista_produtos.html", context)

# Create Data
def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    context = {
        "form": form
    }
    return render(request, 'core/cria_produto.html', context)

def cria_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MarcaForm()
    context = {
        "form": form
    }
    return render(request, 'core/cria_marca.html', context)

# Delete Data
def confirma_deleta_produto(request, id):
    produto = Produto.objects.get(id=id)
    context={
        "produto": produto
    }
    return render(request, 'core/deleta_produto.html', context)

def deleta_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('lista_produtos')

# Update Data
def comprar(request, id):
    produto = Produto.objects.get(id=id)
    produto.em_estoque += 1
    produto.save()
    return redirect('lista_produtos')

def usar(request, id):
    produto = Produto.objects.get(id=id)
    if produto.em_estoque > 0:
        produto.em_estoque -= 1
        produto.save()
    return redirect('lista_produtos')

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(initial={
            "nome": produto.nome,
            "peso": produto.peso,
            "preco": produto.preco,
            "marca": produto.marca,
            "tipo": produto.tipo,
            "em_estoque": produto.em_estoque,
            "necessario": produto.necessario,
        })
    context = {
        "form": form
    }
    return render(request, 'core/edita_produto.html', context)