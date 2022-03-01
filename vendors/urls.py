from django.urls import path
from vendors import views

urlpatterns = [
    path('', views.vendor_home, name='vendor_home'),
    path('create-account/', views.create_vendor_account, name='create_vendor_account'),
    path('login-vendor/', views.login_vendor, name='login_vendor'),
    path('login/', views.login, name='login'),
    path('create-profile/', views.create_vendor_profile, name='create_vendor_profile'),
    path('logout/', views.logout_vendor, name='logout_vendor'),
    path('dashboard/', views.dashboard, name='dashboard'),
]