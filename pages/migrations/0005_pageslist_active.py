# Generated by Django 3.1.2 on 2022-05-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20220507_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageslist',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
