from django.shortcuts import render

# Create your views here.
def products_home(request):

    context = {}

    return render(request, 'products/products_home.html', context)
