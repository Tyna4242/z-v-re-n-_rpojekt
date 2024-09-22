from django.db import models
from django.contrib.auth.models import User

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('l', 'Liter'), ('ml', 'Milliliter')])

    def __str__(self):
        return self.title