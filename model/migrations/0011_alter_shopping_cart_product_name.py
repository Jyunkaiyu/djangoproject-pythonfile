# Generated by Django 4.0.6 on 2022-09-04 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0010_alter_product_dsc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_nameOf', to='model.product'),
        ),
    ]
