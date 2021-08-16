from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.forms import inlineformset_factory

from mainapp.forms import RecordForm
from mainapp.models import CountryRegion, Country


def send_form(request):
    title = 'Форма'
    sent = False
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            sent = True
    context = {'title': title, 'form': form, 'sent': sent}
    return render(request, 'mainapp/form.html', context)


def load_region(request):
    country = request.GET.get('country')
    region_list = None
    if country:
        region_list = CountryRegion.objects.filter(country=country)
    return render(request, 'mainapp/load_region.html', {'region_list': region_list})
