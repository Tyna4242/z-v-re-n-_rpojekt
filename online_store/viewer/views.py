from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def MainPageView(TemplateView):
    template_name = "main.html"
    extra_context = {}