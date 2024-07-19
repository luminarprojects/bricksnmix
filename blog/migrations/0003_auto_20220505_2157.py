# Generated by Django 3.1.2 on 2022-05-05 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220429_0555'),
        ('blog', '0002_auto_20220505_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_Slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=500, null=True, unique=True, verbose_name='Slugfiy'),
        ),
    ]
