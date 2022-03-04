from django.contrib import admin
from .models import VendorProfile, VerifiedBusiness

# Register your models here.
class AdminVendorProfileView(admin.ModelAdmin):

    list_display = ['user', 'business_name', 'business_email', 'business_phone', 'date_joined']
    search_fields = ['user', 'business_name']

class AdminVerifiedBusinessView(admin.ModelAdmin):

    list_display = ['business', 'is_verified']
    search_fields = ['business']

admin.site.register(VendorProfile, AdminVendorProfileView)
admin.site.register(VerifiedBusiness, AdminVerifiedBusinessView)