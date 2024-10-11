from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from .models import Category, Product, Comment
from django.urls import reverse_lazy
from viewer.forms import ProductForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
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

class CategoryView(TemplateView):
    template_name = "viewer/category.html"
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


class PotravinyDetailedView(TemplateView):
  template_name = 'viewer/potraviny_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data( **kwargs)
    context["potraviny_detail"] = Product.objects.get(pk=int(kwargs["pk"]))
    context["potraviny_comments"] = Comment.objects.filter(product__pk=int(kwargs["pk"]))
    return context
  
class CommentCreateView(CreateView):
  template_name = 'viewer/form.html'
  form_class = CommentForm
  success_url = reverse_lazy("potraviny")

  def form_valid(self, form):
    new_comment : Comment = form.save(commit=False)
    new_comment.product = Product.objects.get(pk=int(self.kwargs["product_pk"]))
    new_comment.save()
    return super().form_valid(form)
  

def send_email_to_user(request):
    print(f"Máme nové zboží {Product.objects.all()} ")

    return HttpResponse("vše OK")

def api_get_all_products(request):
  all_products = Product.objects.all()
  json_all_products = {}
  for product in all_products:
    json_all_products[product.pk] = {
      "název": str(product.title),
      "popis": str(product.description)
    }

  return JsonResponse(json_all_products)


def api_get_all_comments(request):
  json_all_comments = { comment.pk: {"text":str(comment.text)} for comment in Comment.objects.all()}
  return JsonResponse(json_all_comments)