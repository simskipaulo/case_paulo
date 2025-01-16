from django.db import models
from django.core.validators import MinValueValidator

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0,0)]
    )
    estoque = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome