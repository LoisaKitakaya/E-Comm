from django.contrib import admin
from .models import Category, Product

# Register your models here.
class AdminProductView(admin.ModelAdmin):

    list_display = ['vendor', 'short_name', 'category', 'product_price', 'date_posted']
    list_filter = ['category', 'vendor']
    search_fields = ['vendor', 'short_name', 'category']

class AdminCategoryView(admin.ModelAdmin):

    list_display = ['category_title']

admin.site.register(Category, AdminCategoryView)

admin.site.register(Product, AdminProductView)