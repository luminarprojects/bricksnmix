# Generated by Django 3.2.12 on 2022-02-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homead_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='CARImage',
            field=models.ImageField(blank=True, help_text='Please use our recommended dimensions: 1372px x 830px', null=True, upload_to='carousel/', verbose_name='Image'),
        ),
    ]
