from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VendorProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account', primary_key=True, blank=True)
    business_name = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to='vendor_profile_image')
    business_email = models.EmailField(max_length=100, unique=True)
    personal_phone = models.CharField(max_length=50, unique=True)
    business_phone = models.CharField(max_length=50, unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:

        ordering = ['-date_joined']

    def __str__(self):

        return self.business_name

class VerifiedBusiness(models.Model):

    business = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='vendor_business')
    is_verified = models.BooleanField(default=False)

    def __str__(self):

        return self.business
