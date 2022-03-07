from django import forms

# forms here
class CheckoutForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=115)
    last_name = forms.CharField(label='Second name', max_length=115)
    email = forms.EmailField(label='Email', max_length=115)
    phone = forms.CharField(label='phone', max_length=15)
    address = forms.CharField(label='Address/street', max_length=115)
    city = forms.CharField(label='City/town', max_length=115)
    place = forms.CharField(label='Place/estate/hose', max_length=225)