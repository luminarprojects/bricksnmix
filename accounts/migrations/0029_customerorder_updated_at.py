# Generated by Django 3.2.25 on 2024-08-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20240812_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
