from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Photo
from django.db.models import Prefetch


class InitiView(ListView):
    template_name = 'initi.html'
    model=Product
    context_object_name='product'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product'] = context['product'].filter(sold=False)
        context['image'] = Photo.objects.filter(cover=True, sold=False)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('busca')
        if search:
            queryset = queryset.filter(name__icontains=search, sold=False)
            print(queryset)
            return queryset
        return queryset
    

class ProductDetailView(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.prefetch_related(Prefetch('foto', queryset=Photo.objects.all()))
    
   

    