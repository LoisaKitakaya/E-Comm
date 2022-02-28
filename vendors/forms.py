from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import VendorProfile

class CreateNewUser(UserCreationForm):

    username = forms.CharField(min_length=5, max_length=100, label='username')
    email = forms.EmailField(max_length=100, label='email')
    first_name = forms.CharField(max_length=100, label='first name')
    last_name = forms.CharField(max_length=100, label='second name')
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    def username_clean(self):

        username = self.cleaned_data['username'].lower()

        new = User.objects.filter(username=username)

        if new.exists():

            raise forms.ValidationError('User already exists')

        return username

    def email_clean(self):

        email = self.cleaned_data['email'].lower()

        new = User.objects.filter(email=email)

        if new.exists():

            raise forms.ValidationError('Email already exists')

        return email

    def clean_password2(self):
        
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:

            raise forms.ValidationError('Passwords do not match')

        return password2

    def save(self, commit=True):
        
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
        )

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data['password1'])

        user.save()

        return user

class CreateVendorProfile(forms.ModelForm):

    class Meta:

        model = VendorProfile

        fields = '__all__'
        exclude = ['user']