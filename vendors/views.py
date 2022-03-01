from django.shortcuts import render, redirect
from django.contrib.auth import logout as dj_logout, login as dj_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from products.models import Product
from .models import VendorProfile
from .forms import CreateNewUser, CreateVendorProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def vendor_home(request):

    context = {}

    return render(request, 'vendors/vendor_home.html', context)

def create_vendor_account(request):

    if request.method == 'POST':

        form = CreateNewUser(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login_vendor')

        else:

            for msg in form.error_messages:
                    
                print(form.error_messages[msg])

    else:

        form = CreateNewUser()

    subtitle = 'Register'

    form_title = 'Register account'

    form_footer = 'Already have an account?'

    redirect_url = "login"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
        'url': redirect_url
    }

    return render(request, 'vendors/vendor_forms.html', context)

def login_vendor(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            dj_login(request, user)

            return redirect('create_vendor_profile')

        else:

            pass

    else:

        form = AuthenticationForm()

    subtitle = 'Login'

    form_title = 'Login'

    form_footer = "Don't have an account?"

    redirect_url = "create"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
        'url': redirect_url
    }

    return render(request, 'vendors/vendor_forms.html', context)

def login(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            dj_login(request, user)

            return redirect('dashboard')

        else:

            pass

    else:

        form = AuthenticationForm()

    subtitle = 'Login'

    form_title = 'Login'

    form_footer = "Don't have an account?"

    redirect_url = "create"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
        'url': redirect_url
    }

    return render(request, 'vendors/vendor_forms.html', context)

@login_required(login_url='login_vendor')
def create_vendor_profile(request):

    logged_in_vendor = request.user

    if request.method == 'POST':

        form = CreateVendorProfile(request.POST, request.FILES)

        if form.is_valid():

            save_instance = form.save(commit=False)
            
            save_instance.user = logged_in_vendor

            save_instance.save()

            return redirect('dashboard')

        else:

            pass

    else:

        form = CreateVendorProfile()

    subtitle = 'Profile'

    form_title = 'Create Profile'

    form_footer = "Already have a profile? To go to dashboard..."

    redirect_url = "dashboard"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
        'url': redirect_url
    }

    return render(request, 'vendors/vendor_forms.html', context)

def logout_vendor(request):

    dj_logout(request)

    return redirect('vendor_home')

@login_required(login_url='login')
def dashboard(request):

    logged_in_user = request.user

    user = User.objects.get(username=logged_in_user)

    print(user)

    user_header = 'Vendor account summary'

    profile = VendorProfile.objects.filter(user=logged_in_user.id)

    print(profile)

    profile_header = 'Business profile summary'

    products = Product.objects.select_related('vendor').filter(vendor=logged_in_user.id)

    products_header = 'Business Products'

    subtitle = 'Dashboard'

    context = {
        'header': subtitle,
        'current_user': user,
        'business_profile': profile,
        'business_products': products,
        # 
        'user_header': user_header,
        'profile_header': profile_header,
        'products_header': products_header,
        'user': logged_in_user,
    }

    return render(request, 'vendors/vendor_dashboard.html', context)