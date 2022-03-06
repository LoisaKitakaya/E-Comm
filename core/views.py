from django.shortcuts import render
from products.models import Product

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

    context = {}

    return render(request, 'core/contacts.html', context)
