# Generated by Django 4.0.2 on 2022-02-28 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_account', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('business_name', models.CharField(max_length=100, unique=True)),
                ('profile_image', models.ImageField(upload_to='vendor_profile_image')),
                ('email_business', models.EmailField(max_length=100, unique=True)),
                ('phone_personal', models.CharField(max_length=50, unique=True)),
                ('phone_business', models.CharField(max_length=50, unique=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='VerifiedBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_business', to='vendors.vendorprofile')),
            ],
        ),
    ]
