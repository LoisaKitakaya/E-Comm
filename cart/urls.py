from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('success/', views.success, name='success'),
]