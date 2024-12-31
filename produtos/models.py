from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Model para categorias de produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

# Model para o produto
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    imagens = models.ImageField(upload_to='produtos/%Y/%m/%d/', blank=True)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

    # Validação personalizada para garantir que o preço e o estoque sejam positivos
    def clean(self):
        if self.preco <= 0:
            raise ValidationError("O preço deve ser maior que zero.")
        if self.estoque < 0:
            raise ValidationError("O estoque não pode ser negativo.")

# Model para o histórico de compras, vinculado ao usuário
class HistoricoCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historico_compras')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.produto.nome}"

    # Validação personalizada para garantir que a quantidade seja válida
    def clean(self):
        if self.quantidade <= 0:
            raise ValidationError("A quantidade de compra deve ser maior que zero.")
