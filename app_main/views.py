from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Product, Photo, Categories, Contact
from django.db.models import Prefetch
from .forms import ContactForm
from django.core.mail import send_mail


class InitiView(ListView):
    template_name = 'initi1.html'
    model=Product
    context_object_name='product'
    queryset = Product.objects.prefetch_related(Prefetch('foto', queryset=Photo.objects.all())).filter(sold=False)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('busca')
        if search:
            queryset = queryset.filter(name__icontains=search, sold=False)
            return queryset
        return queryset
    

class ProductDetailView(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.prefetch_related(Prefetch('foto', queryset=Photo.objects.all())).filter(sold=False)


class CategoryView(ListView):
    template_name = 'category.html'
    model = Product
    context_object_name = 'product'
    queryset = Product.objects.prefetch_related(Prefetch('foto', queryset=Photo.objects.all()))

    def get_queryset(self):
        queryset = super().get_queryset()
        res = self.request.get_full_path_info()
        res = res.split('/')[2]
        queryset = queryset.filter(categorie=res, sold=False)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.all()
        return context
    

class ContactViews(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/'
