from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta():
        model = Product
        # fields = ('name', 'price', 'stock')
        fields = '__all__'
        widgets = {
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-control d-flex'}),
            'name': forms.TextInput(attrs={'placeholder': 'Please input a name of product'}),
            'description': forms.Textarea(attrs={'placeholder': 'Please input the description of product'}),
            'calories': forms.NumberInput(attrs={'placeholder': 'Please enter the number of calories'}),
            'spiciness_level': forms.NumberInput(attrs={'placeholder': 'Please enter the spiciness level (1-5)'}),
            'protein': forms.NumberInput(attrs={'placeholder': 'Please enter the amount of protein'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Please enter a price'}),
            # 'stock': forms.NumberInput(attrs={'placeholder': 'Please enter a product quantity'}),
        }