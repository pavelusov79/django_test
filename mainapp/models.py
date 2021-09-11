import re

from django.core.exceptions import ValidationError
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=64, verbose_name='страна')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'Страны'


class CountryRegion(models.Model):
    region_name = models.CharField(max_length=64, verbose_name='регион страны')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_region')

    class Meta:
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.region_name


def validate_field(value):
    result = re.match("^[a-zA-Zа-яА-Я]+|[a-zA-Zа-яА-Я]+$", value)
    if not result:
        raise ValidationError('Допускается только кирилица или латиница. Допускается два слова.',
                              params={'value': value})


class Product(models.Model):
    YEAR_CHOICES = {
        (2018, 2018),
        (2019, 2019),
        (2020, 2020),
        (2021, 2021)
    }
    product_name = models.CharField(max_length=64, verbose_name='Название товара', validators=[validate_field])
    product_grade = models.CharField(max_length=128, verbose_name='Марка товара', blank=True,
                                     validators=[validate_field])
    product_year = models.PositiveIntegerField(verbose_name='Год изготовления', choices=YEAR_CHOICES, blank=True,
                                               null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_product')
    region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, related_name='region_product')

    class Meta:
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name
