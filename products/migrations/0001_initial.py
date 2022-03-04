# Generated by Django 4.0.2 on 2022-03-04 10:42

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import slugger.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, unique=True)),
                ('short_name_slug', slugger.fields.AutoSlugField(populate_from='short_name')),
                ('full_name', models.CharField(max_length=250, unique=True)),
                ('product_thumbnail', models.ImageField(upload_to='product_thumbnail')),
                ('product_price', models.IntegerField(default=0)),
                ('product_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('vendor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='owning_business', to='vendors.vendorprofile')),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
