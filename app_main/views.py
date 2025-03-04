from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Photo
from django.db.models import Prefetch


class InitiView(ListView):
    template_name = 'initi.html'
    model=Product
    context_object_name='product'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product'] = context['product'].filter(sold=False)
        dici: dict = dict()
        context['image'] = Photo.objects.filter(cover=True)
        return context
