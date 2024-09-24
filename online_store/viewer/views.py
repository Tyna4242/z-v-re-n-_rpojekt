from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Category, Product
from django.urls import reverse_lazy
from viewer.forms import ProductForm
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

class ProductCreateView(CreateView):
    template_name = 'viewer/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')


class ProductUpdateView(UpdateView):
    template_name = 'viewer/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')


class ProductDeleteView(DeleteView):
    template_name = 'viewer/product_confirm_delete.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')