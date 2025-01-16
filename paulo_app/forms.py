from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']
    
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise forms.ValidationError('Preço não pode ser negativo.')
        return preco
    
    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque < 0:
            raise forms.ValidationError("O estoque não pode ser negativo.")
        return estoque