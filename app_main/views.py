from django.shortcuts import render
from django.views.generic import TemplateView


class InitiView(TemplateView):
    template_name = 'initi.html'
