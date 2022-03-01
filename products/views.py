from django.shortcuts import redirect, render
from .forms import CreateProduct
from .models import VendorProfile

# Create your views here.
def products_home(request):

    context = {}

    return render(request, 'products/products_home.html', context)

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
