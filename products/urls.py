from django.urls import path
from products import views

urlpatterns = [
    path('add-product/', views.create_product, name='create_product'),
    path('edit-product/<slug:short_name_slug>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('all-products/', views.products, name='products'),
    path('search-filter/', views.search, name='search'),
    path('product-details/<slug:short_name_slug>/', views.product_details, name='product_details'),
]