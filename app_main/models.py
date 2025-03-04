from django.db import models


class CategoriesModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tipo', unique=True)

    class Meta:
        odering=['name']
        verbose_name='Categorias'

    def __str__(self):
        return self.name


class SellerModel(models.Model):
    name=models.CharField(max_length=200, unique=True, verbose_name='Nome')
    fone = models.CharField(max_length=20, unique=True, verbose_name='Telefone')
    street = models.CharField(max_length=200, verbose_name='Rua', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    district = models.CharField(max_length=100, verbose_name='Bairro', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='Cidade', null=True, blank=True)
    cep = models.CharField(max_length=8, verbose_name='CEP')

    class Meta:
        odering=['name']
        verbose_name='Vendedor'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kargs):
        self.name = self.name.title()
        super().save(*args, **kargs)


class ProductModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    categorie = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, verbose_name='Categoria')
    sold = models.BooleanField(default=False, verbose_name='Vendido')
    description = models.TextField(max_length=200, verbose_name='Descrição')

class PhotoModel(models.Model):
    product = models.ForeignKey(ProductModel, )
    cover = models.BooleanField(default=False, verbose_name='Capa')
    photo = models.ImageField(upload_to='products/', verbose_name='Foto')

