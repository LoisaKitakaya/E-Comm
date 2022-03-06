from django import forms
from .models import Product

# create your forms
class CreateProduct(forms.ModelForm):

    class Meta:

        model = Product

        fields = '__all__'
        exclude = ['short_name_slug', 'vendor']

class AddToCart(forms.Form):

    quantity = forms.IntegerField(label='Quantity')