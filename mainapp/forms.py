from django import forms
from django.core.validators import RegexValidator

from mainapp.models import Product, Country, CountryRegion


class RecordForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'country': 'Cтрана',
            'region': 'Регион страны'
        }

        help_texts = {
            'product_year': 'поле необязательное',
        }

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['product_name'] = forms.CharField(label='Название товара', validators=[
            RegexValidator(regex='^[a-zA-Zа-яА-Я]+$', message='Допускается только кирилица или латиница. '
                                                              'Допускается одно слово.')])
        self.fields['product_grade'] = forms.CharField(label='Марка', validators=[
            RegexValidator(regex='^[a-zA-Zа-яА-Я]+|[a-zA-Zа-яА-Я]+$', message='Допускается только кирилица или '
                                                                              'латиница. Допускается два слова.')])
        self.fields['region'].queryset = CountryRegion.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['region'].queryset = CountryRegion.objects.filter(
                    country_id=country_id).order_by('region_name')
            except (ValueError, TypeError):
                pass

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

