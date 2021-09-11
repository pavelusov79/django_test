from django import forms
from django.core.validators import RegexValidator

from mainapp.models import Product, CountryRegion


class RecordForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        help_texts = {
            'product_year': 'поле необязательное',
        }

        labels = {
            'region': 'Регион страны',
            'country': 'Cтрана',
        }

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # if 'country' in self.data:
        #     try:
        #         country_id = int(self.data.get('country'))
        #         self.fields['region'].queryset = CountryRegion.objects.filter(
        #             country_id=country_id).order_by('region_name')
        #     except (ValueError, TypeError):
        #         pass






