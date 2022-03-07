from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderAdminView(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'email', 'phone', 'paid_amount', 'created_at']
    list_filter = ['first_name', 'created_at', 'vendors']
    search_fields = ['first_name', 'email', 'vendors']

class OrderItemAdminView(admin.ModelAdmin):

    list_display = ['order', 'product', 'vendor', 'vendor_paid', 'price', 'quantity']
    list_filter = ['order', 'product', 'vendor']
    search_fields = ['order', 'product', 'vendor']

admin.site.register(Order, OrderAdminView)
admin.site.register(OrderItem, OrderItemAdminView)