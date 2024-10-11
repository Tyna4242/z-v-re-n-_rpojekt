from django.contrib import admin
from .models import Category, Product, PotravinyFeatures, Comment

# Register your models here
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PotravinyFeatures)
admin.site.register(Comment)
