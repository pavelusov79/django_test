# Generated by Django 3.2.6 on 2021-08-17 23:52

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_product_product_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_grade',
            field=models.CharField(blank=True, max_length=128, validators=[mainapp.models.validate_field], verbose_name='Марка товара'),
        ),
    ]