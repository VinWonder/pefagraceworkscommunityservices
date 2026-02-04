from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import DonationForm


class DonateView(CreateView):
    template_name = 'donations/donate.html'
    form_class = DonationForm
    success_url = reverse_lazy('donations:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Make a Donation'
        return context


class DonationSuccessView(TemplateView):
    template_name = 'donations/success.html'
