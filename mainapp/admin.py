from django.contrib import admin

from mainapp.models import Country, CountryRegion, Product


admin.site.register(Country)
admin.site.register(CountryRegion)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_grade', 'country', 'region')
    list_filter = ('country',)
