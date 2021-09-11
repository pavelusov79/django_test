from django.shortcuts import render
from django.views.generic import CreateView

from mainapp.forms import RecordForm
from mainapp.models import CountryRegion


class CreateProduct(CreateView):
    sent = False
    template_name = 'mainapp/form.html'
    form_class = RecordForm
    success_url = 'send_form'

    def form_valid(self, form):
        self.sent = True
        super(CreateProduct, self).form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(CreateProduct, self).get_context_data(**kwargs)
        context['sent'] = self.sent
        return context


def load_region(request):
    country = request.GET.get('country')
    region_list = None
    if country:
        region_list = CountryRegion.objects.filter(country=country)
    return render(request, 'mainapp/load_region.html', {'region_list': region_list})
