from dataclasses import field
from django import forms

from core.models import Produto, Marca


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'peso', 'preco', 'marca', 'tipo', 'em_estoque', 'necessario']

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = ['nome']