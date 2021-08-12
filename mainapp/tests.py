from django.test import TestCase
from django.test.client import Client
from mainapp.models import Product, Country, CountryRegion


class MainappTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        country = Country.objects.create(country_name='Россия')
        country1 = Country.objects.create(country_name='США')
        for i in range(1, 11):
            region_i = CountryRegion.objects.create(region_name=f'region_{i}', country=country)
            Product.objects.create(product_name=f'product_{i}', product_grade=f'product_grade_{i}', product_year=2020,
                                   country=country, region=region_i)
        for j in range(11, 21):
            region_j = CountryRegion.objects.create(region_name=f'region_{j}', country=country1)
            Product.objects.create(product_name=f'product_{j}', product_grade=f'product_grade_{j}', country=country,
                                   region=region_j)

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
