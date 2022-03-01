from django.db import models
from vendors.models import VendorProfile
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):

    category_title = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=250)

    def __str__(self):

        return self.category_title

class Product(models.Model):

    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='owning_business', blank=True)
    short_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=250, unique=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_thumbnail = models.ImageField(upload_to='product_thumbnail')
    product_price = models.IntegerField(default=0)
    product_description = RichTextUploadingField()
    date_posted = models.DateField(auto_now_add=True)

    class Meta:

        ordering = ['-date_posted']

    def __str__(self):

        return self.short_name