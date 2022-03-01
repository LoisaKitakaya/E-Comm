from django.urls import path
from products import views

urlpatterns = [
    path('', views.products_home, name='products_home'),
]