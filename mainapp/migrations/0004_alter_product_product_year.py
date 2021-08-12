# Generated by Django 3.2.6 on 2021-08-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_product_product_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_year',
            field=models.PositiveIntegerField(blank=True, choices=[(2020, 2020), (2019, 2019), (2021, 2021), (2018, 2018)], null=True, verbose_name='Год изготовления'),
        ),
    ]
