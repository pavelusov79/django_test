from rest_framework import generics, permissions

from mainapp.models import Country, CountryRegion, Product
from . import serializers


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAdminUser]


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAdminUser]


class CountryRegionList(generics.ListCreateAPIView):
    queryset = CountryRegion.objects.all()
    serializer_class = serializers.CountryRegionSerializer
    permission_classes = [permissions.IsAdminUser]


class CountryRegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CountryRegion.objects.all()
    serializer_class = serializers.CountryRegionSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAdminUser]
