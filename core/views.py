from django.shortcuts import render, redirect
from products.models import Product
from .forms import ContactForm

# Create your views here.
def home(request):

    section_1 = Product.objects.all()[:3]

    section_2 = Product.objects.all()[3:6]

    section_3 = Product.objects.all()[6:9]

    context = {
        'first_section_objects': section_1,
        'second_section_objects': section_2,
        'third_section_objects': section_3,
    }

    return render(request, 'core/index.html', context)

def about(request):

    context = {}

    return render(request, 'core/about.html', context)

def contacts(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']

            second_name = form.cleaned_data['second_name']

            user_email = form.cleaned_data['email']

            subject = form.cleaned_data['subject']

            user_message = form.cleaned_data['the_message']

            return redirect('home')

    else:

        form = ContactForm()

    form_title = 'Contact'

    context = {
        'form': form,
        'form_title': form_title,
    }

    return render(request, 'core/contacts.html', context)
