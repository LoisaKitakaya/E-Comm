from django.urls import path
from vendors import views

urlpatterns = [
    path('', views.vendor_home, name='vendor_home'),
]