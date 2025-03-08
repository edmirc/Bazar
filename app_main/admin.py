from django.contrib import admin
from .models import Categories, Seller, Product, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra=1


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_filter=['name']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_filter=['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[PhotoInline]
    list_filter=['name', 'seller', 'sold']
    list_display=['name', 'price', 'seller', 'categorie', 'sold']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter=['product']
    list_display=['product', 'cover', 'sold', 'photo']


admin.site.site_header = 'Painel de Administração do Bazar da Ana'
admin.site.site_title = 'Bazar da Ana'
