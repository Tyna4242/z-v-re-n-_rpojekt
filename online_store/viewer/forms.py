from django.forms import ModelForm
from viewer.models import Category, Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'