# Generated by Django 5.0 on 2024-02-24 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_rename_catogry_product_categry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categry',
            new_name='category',
        ),
    ]