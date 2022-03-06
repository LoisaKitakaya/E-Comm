from django.shortcuts import render,redirect
from django.contrib import messages
from .cart import Cart

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

    context = {}

    return render(request, 'cart/cart.html', context)