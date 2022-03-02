from django.shortcuts import redirect, render, get_object_or_404
from .forms import CreateProduct
from .models import VendorProfile, Category, Product

# Create your views here.
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

    subtitle = 'Create Product'

    form_footer = 'Go back to dashboard?'

    redirect_url = 'dashboard'

    context = {
        'form': form,
        'form_title': subtitle,
        'form_footer': form_footer,
        'url': redirect_url,
    }

    return render(request, 'products/products_forms.html', context)

def categories(request, category_slug):

    category_filter = get_object_or_404(Category, category_slug=category_slug)

    return render(request, 'products/products_home.html', {'category_filter': category_filter})

def products(request):

    product_filter = Product.objects.all()

    context = {
        'all_products': product_filter,
    }

    return render(request, 'products/products_home.html', context)
