from django.contrib import admin
from .models import Category, Product

# Register your models here.
class AdminProductView(admin.ModelAdmin):

    list_display = ('vendor', 'short_name', 'product_category', 'product_price', 'date_posted')
    list_filter = ('product_category', 'product_price')

class AdminCategoryView(admin.ModelAdmin):

    prepopulated_fields = {'category_slug': ('category_title',)}

admin.site.register(Category, AdminCategoryView)

admin.site.register(Product, AdminProductView)