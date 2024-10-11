from django.forms import ModelForm
from viewer.models import Category, Product, Comment
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Název produktu musí mít alespoň 3 znaky.')
        return title
    


class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['text']









