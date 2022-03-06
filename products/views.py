from django.shortcuts import redirect, render
from .forms import CreateProduct, AddToCart
from .models import VendorProfile, Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages

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

            messages.success(request, 'Product added successfully.')

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

            messages.info(request, 'Product edited successfully.')

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

    messages.error(request, 'Product has been deleted.')

    return redirect('dashboard')

def products(request):

    product_filter = Product.objects.all()

    error_message = "OOPS! Couldn't find E-Comm the product. Something is wrong on our end. We are sorry for the inconvinience and are doing everything to re-establish the E-Comm. shopping experience. Check back in a few."

    context = {
        'all_products': product_filter,
        'error_message': error_message,
    }

    return render(request, 'products/products_home.html', context)

def product_details(request, short_name_slug):

    prod_item = Product.objects.get(short_name_slug=short_name_slug)

    cart = Cart(request)

    if request.method == 'POST':

        form = AddToCart(request.POST)

        if form.is_valid():

            quantity = form.cleaned_data['quantity']

            print(quantity)

            cart.add(product_id=prod_item.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'Product added to cart.')

    else:

        form = AddToCart()

    context = {
        'product_details': prod_item,
        'form': form,
    }

    return render(request, 'products/products_detail.html', context)

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

    error_message = "What you are looking for doesn't exist in the E-Comm. Store. Try searching by category, product name, or vendor name."
        
    context = {
        'all_products': filter_results,
        'error_message': error_message,
    }

    return render(request, 'products/products_home.html', context)