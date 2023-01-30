from django.contrib import admin

from mainapp.forms import RecordForm
from mainapp.models import Country, CountryRegion, Product, Seeker


admin.site.register(Country)


@admin.register(CountryRegion)
class CountryRegionAdmin(admin.ModelAdmin):
    list_display = ('region_name', 'country')
    list_filter = ('country',)
    search_fields = ('region_name__startswith',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_grade', 'country',)
    list_filter = ('country',)
    form = RecordForm
    search_fields = ('product_name__startswith', 'product_grade__startswith',)

    class Media:
        js = ('js/script.js', 'js/jquery-3.6.0-min.js')


def name(obj):
    return f'{obj.user.first_name} {obj.user.last_name}'


@admin.register(Seeker)
class SeekerAdmin(admin.ModelAdmin):
    list_display = (name, 'user')
