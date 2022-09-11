from multiprocessing import context
from django.shortcuts import render

from core.models import Produto
from core.forms import ProdutoForm

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, "core/lista_produtos.html", context)

def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutoForm()
    context = {
        "form": form
    }
    return render(request, 'core/cria_tarefa.html', context)