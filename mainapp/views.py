from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.forms import inlineformset_factory

from mainapp.forms import RecordForm, UserForm, SeekerForm
from mainapp.models import CountryRegion, Seeker, User


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


# class UserCreateView(CreateView):
#     template_name = 'mainapp/user_create_form.html'
#     form_class = UserForm
#     success_url = 'send_form'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['seeker_form'] = SeekerForm()
#         return context
#
#     def form_valid(self, form):
#         user = form.save(commit=False)
#         seeker_form = SeekerForm(self.request.POST, instance=user)
#         if seeker_form.is_valid():
#             user.is_active = False
#             user.save()
#             print('valid')
#             Seeker.objects.create(user=user,
#                                   age=seeker_form.cleaned_data['age'],
#                                   skills=seeker_form.cleaned_data['skills'])
#             return HttpResponseRedirect(reverse(self.success_url))
#         return render(self.request, self.template_name, {'form': form, 'seeker_form': seeker_form})


class UserCreateView(CreateView):
    template_name = 'mainapp/user_create_form.html'
    form_class = UserForm
    # success_url = 'send_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['seeker_form'] = SeekerForm(self.request.POST)
        else:
            context['seeker_form'] = SeekerForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        seeker_form = context['seeker_form']
        if form.is_valid() and seeker_form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            seeker = seeker_form.save(commit=False)
            seeker.user = user
            seeker.save()
            return super().form_valid(form)
            # return HttpResponseRedirect(reverse('send_form'))
        return render(self.request, self.template_name, context)

    def get_success_url(self):
        return reverse('send_form')