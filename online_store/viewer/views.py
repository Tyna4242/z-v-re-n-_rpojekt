from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product
# Create your views here.

class MainPageView(TemplateView):
    template_name = "viewer/main.html"
    extra_context = {}

class BasePageView(TemplateView):
    template_name = "base.html"
    extra_context = {}

class PotravinyView(TemplateView):
    template_name = "viewer/potraviny.html"
    extra_context = {
        'all_category': Category.objects.all(),
        'all_product': Product.objects.all()
    }
