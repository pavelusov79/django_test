from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=64, verbose_name='страна')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'Страны'


class CountryRegion(models.Model):
    region_name = models.CharField(max_length=64, verbose_name='регион страны')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.region_name} ({self.country.country_name})'

    class Meta:
        verbose_name_plural = 'Регионы страны'


class Product(models.Model):
    YEAR_CHOICES = {
        (2018, 2018),
        (2019, 2019),
        (2020, 2020),
        (2021, 2021)
    }
    product_name = models.CharField(max_length=64, verbose_name='Название товара')
    product_grade = models.CharField(max_length=128, verbose_name='Марка товара', blank=True)
    product_year = models.PositiveIntegerField(verbose_name='Год изготовления', choices=YEAR_CHOICES, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_name} ({self.country.country_name}, {self.region.region_name})'

    class Meta:
        verbose_name_plural = 'Товары'
