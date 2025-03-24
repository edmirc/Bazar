from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tipo', unique=True)

    class Meta:
        ordering=['name']
        verbose_name='Categorias'
        verbose_name_plural='Categorias'

    def save(self, *args, **kargs):
        self.name = self.name.strip().title()
        super().save(*args, **kargs)


    def __str__(self):
        return self.name


class Seller(models.Model):
    name=models.CharField(max_length=200, unique=True, verbose_name='Nome')
    fone = models.CharField(max_length=20, unique=True, verbose_name='Telefone')
    street = models.CharField(max_length=200, verbose_name='Rua', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    district = models.CharField(max_length=100, verbose_name='Bairro', null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name='Cidade', null=True, blank=True)
    cep = models.CharField(max_length=8, verbose_name='CEP')

    class Meta:
        ordering=['name']
        verbose_name='Vendedor'
        verbose_name_plural='vendedor'
    
    def __str__(self):
        return self.name

    def save(self, *args, **kargs):
        self.name = self.name.title().strip()
        super().save(*args, **kargs)


class Product(models.Model):
    status_choice = (('Novo', 'Novo'), ('Usado', 'Usado'), ('Semi-novo', 'Semi-novo'), ('Quebrado', 'Quebrado'))
    name = models.CharField(max_length=200, verbose_name='Nome')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Vendedor')
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Categoria')
    size = models.CharField(max_length=20, verbose_name='Tamanho', null=True, blank=True)
    brand = models.CharField(max_length=100, verbose_name="Marca", null=True, blank=True)
    condition=models.CharField(max_length=20, choices=status_choice, verbose_name='Condição')
    sold = models.BooleanField(default=False, verbose_name='Vendido')
    description = models.TextField(max_length=800, verbose_name='Descrição')

    class Meta:
        ordering=['name']
        verbose_name='Produto'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kargs):
        self.name = self.name.strip().title()
        self.brand = self.brand.strip().title()
        self.size = self.size.strip().title()
        if self.sold:
            for photo in Photo.objects.filter(product=self):
                photo.sold = True
                photo.save()
        super().save(*args, **kargs)


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produto', related_name='foto')
    cover = models.BooleanField(default=False, verbose_name='Capa')
    sold = models.BooleanField(default=False, verbose_name='Vendido')
    photo = models.ImageField(upload_to='products/', verbose_name='Foto')

    class Meta:
        ordering=['product']
        verbose_name='Imagem'
        verbose_name_plural = 'Imagens'

    def save(self, *args, **kargs):
        if self.cover:
            try:
                temp = Photo.objects.get(product=self.product, cover=True)
                if self != temp:
                    temp.cover = False
                    temp.save()
            except:
                pass
        return super().save(*args, **kargs)

    def __str__(self):
        return self.product.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    message = models.TextField(max_length=200, verbose_name='Mensagem')
    seen = models.BooleanField(default=False, verbose_name='Visto')

    class Meta:
        ordering=['name']
        verbose_name='Contato'
        verbose_name_plural='Contatos'

    def __str__(self):
        return self.name

    def save(self, *args, **kargs):
        self.name = self.name.strip().title()
        super().save(*args, **kargs)