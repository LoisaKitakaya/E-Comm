from django.shortcuts import redirect, render
from .forms import CreateProduct
from .models import VendorProfile, Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as dj_logout, login as dj_login

# Create your views here.
@login_required(login_url='login')
def create_product(request):

    logged_in_user = request.user

    if request.method == 'POST':

        form = CreateProduct(request.POST, request.FILES)

        if form.is_valid():

            save_instance = form.save(commit=False)

            profile = VendorProfile.objects.get(user=logged_in_user)

            save_instance.vendor = profile

            save_instance.save()

            return redirect('dashboard')

        else:

            pass

    else:

        form = CreateProduct()

    subtitle = 'Add Product'

    form_footer = 'Go back to dashboard?'

    redirect_url = 'dashboard'

    context = {
        'form': form,
        'form_title': subtitle,
        'form_footer': form_footer,
        'url': redirect_url,
    }

    return render(request, 'products/products_forms.html', context)

def products(request):

    product_filter = Product.objects.all()

    context = {
        'all_products': product_filter,
    }

    return render(request, 'products/products_home.html', context)

@login_required(login_url='login')
def edit_product(request, short_name_slug):

    logged_in_user = request.user

    edit_instance = Product.objects.get(short_name_slug=short_name_slug)

    if request.method == 'POST':

        form = CreateProduct(request.POST, request.FILES, instance=edit_instance)

        if form.is_valid():

            save_instance = form.save(commit=False)

            profile = VendorProfile.objects.get(user=logged_in_user)

            save_instance.vendor = profile

            save_instance.save()

            return redirect('dashboard')

        else:

            pass

    else:

        form = CreateProduct()

    subtitle = 'Edit Product'

    form_footer = 'Go back to dashboard?'

    redirect_url = 'dashboard'

    context = {
        'form': form,
        'form_title': subtitle,
        'form_footer': form_footer,
        'url': redirect_url,
    }

    return render(request, 'products/products_forms.html', context)

@login_required(login_url='login')
def delete_product(request, id):

    to_delete = Product.objects.get(id=id)

    to_delete.delete()

    return redirect('dashboard')

def products(request):

    product_filter = Product.objects.all()

    context = {
        'all_products': product_filter,
    }

    return render(request, 'products/products_home.html', context)

def search(request):

    if request.method == 'GET':

        query = request.GET.get('query')

        filter_results = Product.objects.filter(
            Q(category__category_title__icontains=query) | 
            Q(short_name__icontains=query) | 
            Q(full_name__icontains=query)
        )

    else:

        filter_results = []
        
    context = {
        'all_products': filter_results,
    }

    return render(request, 'products/products_home.html', context)