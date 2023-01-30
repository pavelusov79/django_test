from rest_framework import serializers

from mainapp.models import Product, Country, CountryRegion


class CountrySerializer(serializers.ModelSerializer):
    # country_region = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # country_product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class CountryRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryRegion
        fields = ('country', 'region_name')


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('product_name', 'product_grade', 'product_year', 'country', 'region')