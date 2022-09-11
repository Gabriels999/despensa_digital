from dataclasses import field
from django import forms

from core.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'peso', 'preco', 'marca', 'tipo']