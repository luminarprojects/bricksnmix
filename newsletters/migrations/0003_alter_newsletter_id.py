# Generated by Django 3.2.14 on 2022-08-14 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20220502_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
