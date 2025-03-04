from django.contrib import admin
from .models import Categories, Seller, Product, Photo


class CategoriesAdmin(admin.ModelAdmin):
    list_filter=['name']


class SellerAdmin(admin.ModelAdmin):
    list_filter=['name']

class ProductAdmin(admin.ModelAdmin):
    list_filter=['name', 'seller', 'sold']
    list_display=['name', 'price', 'seller', 'categorie', 'sold']


class PhotoAdmin(admin.ModelAdmin):
    list_filter=['product']

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Photo, PhotoAdmin)
