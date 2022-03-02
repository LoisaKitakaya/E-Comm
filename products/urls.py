from django.urls import path
from products import views

urlpatterns = [
    path('', views.products_home, name='products_home'),
    path('create-product', views.create_product, name='create_product'),
    path('<slug:category_slug>/', views.categories, name='categories'),
    path('e-com/all/', views.products, name='products'),
]