# Generated by Django 4.0.6 on 2022-08-13 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_shopping_cart_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopping_cart',
            old_name='count',
            new_name='counts',
        ),
    ]