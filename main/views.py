from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from django.urls import reverse_lazy
from .models import Testimonial, FocusArea
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get featured testimonials
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:3]

        # Get impact stats (you can make these dynamic too)
        context['impact_stats'] = [
            {'number': '100%', 'label': 'of donations go to mission work'},
            {'number': '500+', 'label': 'Lives transformed annually'},
            {'number': '50+', 'label': 'Communities served'},
            {'number': '10+', 'label': 'Years of service'}
        ]

        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'


class WorkView(TemplateView):
    template_name = 'main/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['focus_areas'] = FocusArea.objects.filter(is_active=True).order_by('order')
        return context


class MediaView(TemplateView):
    template_name = 'main/media.html'  # Updated path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Media & Gallery'
        return context


class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        context['site_name'] = 'PEFA GraceWorks Community Services'
        context['address'] = 'PEFA Church Nyamasaria, Kisumu-Kakamega Road, Nyamasaria, Kisumu County, Kenya'
        context['contact_phone'] = '0728 565 413'
        context['contact_email'] = 'info@pefagraceworks.org'
        return context

    def form_valid(self, form):
        # Here you can process the form data (send email, save to database, etc.)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # For now, just show a success message
        messages.success(self.request, f'Thank you {name}! Your message has been sent. We will get back to you soon.')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class ContactSuccessView(TemplateView):
    template_name = 'main/contact_success.html'

class BeliefView(TemplateView):
    template_name = 'main/belief.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Belief'
        return context


class FaithOutreachView(TemplateView):
    template_name = 'main/faith_outreach.html'  # Or 'main/faith_outreach.html' if in a subfolder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Faith & Outreach'
        return context

class WaterSanitationView(TemplateView):
    template_name = 'main/water_sanitation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Water & Sanitation'
        return context


class HealthServicesView(TemplateView):
    template_name = 'main/health_services.html'  # Or 'main/health_services.html' if in a subfolder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Health Services'
        return context


class EducationSupportView(TemplateView):
    template_name = 'main/education_support.html'  # Or 'main/education_support.html' if in a subfolder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Education Support'
        return context



