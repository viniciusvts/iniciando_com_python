from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='nome')
    descricao = models.TextField(null=True, verbose_name='descrição')
    is_active = models.BooleanField(default=True, verbose_name='ativo')

    # toString do python
    # na página do CRUD categoria erá aparecer o name na lista
    # ao invés de "object()category"
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        
class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='nome')

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='nome')
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='preço')
    is_active = models.BooleanField(default=True, verbose_name='ativo')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'