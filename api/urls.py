from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'api'

urlpatterns = [
    path('countries/', views.CountryList.as_view(), name="countries"),
    path('country/<int:pk>/', views.CountryDetail.as_view()),
    path('regions/', views.CountryRegionList.as_view(), name='regions'),
    path('region/<int:pk>/', views.CountryRegionDetail.as_view()),
    path('products/', views.ProductList.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
