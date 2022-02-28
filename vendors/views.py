from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateNewUser, CreateVendorProfile

# Create your views here.
def vendor_home(request):

    context = {}

    return render(request, 'vendors/vendor_home.html', context)

def create_vendor_account(request):

    if request.method == 'POST':

        form = CreateNewUser(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login_vendor   ')

        else:

            for msg in form.error_messages:
                    
                print(form.error_messages[msg])

    else:

        form = CreateNewUser()

    subtitle = 'Register'

    form_title = 'Register account'

    form_footer = 'Already have an account?'

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
    }

    return render(request, 'vendors/vendor_forms.html', context)

def login_vendor(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            django_login(request, user)

            return redirect('dashboard')

        else:

            pass

    else:

        form = AuthenticationForm()

    subtitle = 'Login'

    form_title = 'Login'

    form_footer = "Don't have an account?"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
    }

    return render(request, 'vendors/vendor_forms.html', context)

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

    form_footer = "Go to dashboard?"

    context = {
        'header': subtitle,
        'form': form,
        'form_title': form_title,
        'form_footer': form_footer,
    }

    return render(request, 'vendors/vendor_forms.html', context)