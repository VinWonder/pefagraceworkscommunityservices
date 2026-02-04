from django.shortcuts import render
from django.views.generic import TemplateView


class FoodBankView(TemplateView):
    template_name = 'outreach/food_bank.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Food Bank'
        return context
