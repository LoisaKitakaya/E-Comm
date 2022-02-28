from django.shortcuts import render

# Create your views here.
def vendor_home(request):

    context = {}

    return render(request, 'vendors/vendor_home.html', context)