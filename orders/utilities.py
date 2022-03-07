from cart.cart import Cart
from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, address, city, place, phone, amount):

    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, city=city, place=place, phone=phone, paid_amount=amount)

    for item in Cart(request):

        OrderItem.objects.create(order=order, product=item['product'], vendor=item['product'].vendor, price=item['product'].product_price, quantity=item['quantity'])
    
        order.vendors.add(item['product'].vendor)

    return order