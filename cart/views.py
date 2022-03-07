from django.shortcuts import render,redirect
from django.contrib import messages
from .cart import Cart
from .forms import CheckoutForm
from orders.utilities import checkout

# Create your views here.
def cart(request):

    cart = Cart(request)

    if request.method == 'GET':

        delete_item = request.GET.get('delete', '')

        if delete_item:

            cart.remove(delete_item)

            messages.error(request, 'Item removed from cart.')

            return redirect('cart')

        change_quantity = request.GET.get('change_quantity', '')

        quantity = request.GET.get('quantity', 0)

        if change_quantity:
            
            cart.add(change_quantity, quantity, True)

            return redirect('cart')

    if request.method == 'POST':

        form = CheckoutForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            place = form.cleaned_data['place']

            order = checkout(request, first_name, last_name, email, address, city, place, phone, cart.get_total_cost())

            messages.success(request, 'Order submitted successfully.')

            cart.clear()

            return redirect('success')

    else:

        form = CheckoutForm()

    context = {
        'form': form,
    }

    return render(request, 'cart/cart.html', context)

def success(request):

    context = {}

    return render(request, 'cart/success.html', context)