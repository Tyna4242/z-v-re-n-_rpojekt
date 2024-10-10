from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Category, Product
from django.urls import reverse_lazy
from viewer.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'viewer/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')


class ProductUpdateView(UpdateView):
    template_name = 'viewer/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'viewer/product_confirm_delete.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('potraviny-view')
    permission_required = 'viewer.potraviny-delete-view'  # Název oprávnění (nahraď 'app_name' názvem své aplikace)

class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {}

class SignUpView(CreateView):
  model = User
  template_name = 'viewer/form.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('login')