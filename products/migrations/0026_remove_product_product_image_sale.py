# Generated by Django 3.2.12 on 2022-02-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20220217_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image_sale',
        ),
    ]
