from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from mainapp.models import Product, Seeker


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


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Адрес эллектронной почты', required=True)
        self.fields['first_name'] = forms.CharField(max_length=20, label='Фамилия', required=True)
        self.fields['last_name'] = forms.CharField(max_length=20, label='Имя', required=True)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = ('age', 'skills')

    def __init__(self, *args, **kwargs):
        super(SeekerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('вы слишком молоды')
        return age

