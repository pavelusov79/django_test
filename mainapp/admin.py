from django.contrib import admin

from mainapp.forms import RecordForm
from mainapp.models import Country, CountryRegion, Product


admin.site.register(Country)
admin.site.register(CountryRegion)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_grade', 'country',)
    list_filter = ('country',)
    form = RecordForm

    class Media:
        js = ('js/script.js', 'js/jquery-3.6.0-min.js')
