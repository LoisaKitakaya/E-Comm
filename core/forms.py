from cProfile import label
import email
from django import forms

# forms here
class ContactForm(forms.Form):

    first_name = forms.CharField(label='First name', max_length=50)
    second_name = forms.CharField(label='Second name', max_length=50)
    email = forms.EmailField(label='Email', max_length=150)
    subject = forms.CharField(label='Subject', max_length=150)
    the_message = forms.CharField(label='Your message', widget=forms.Textarea())