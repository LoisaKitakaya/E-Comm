from django.contrib import admin
from .models import VendorProfile, VerifiedBusiness

# Register your models here.
class AdminVendorProfileView(admin.ModelAdmin):

    list_display = ('user', 'business_name', 'business_email', 'business_phone', 'date_joined')

class AdminVerifiedBusinessView(admin.ModelAdmin):

    list_display = ('business', 'is_verified')

admin.site.register(VendorProfile, AdminVendorProfileView)
admin.site.register(VerifiedBusiness, AdminVerifiedBusinessView)