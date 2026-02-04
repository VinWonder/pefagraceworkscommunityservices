from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('work/', WorkView.as_view(), name='work'),
    path('media/', MediaView.as_view(), name='media'),
    path('belief/', BeliefView.as_view(), name='belief'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
    path('water-sanitation/', WaterSanitationView.as_view(), name='water_sanitation'),
    path('faith-outreach/', FaithOutreachView.as_view(), name='faith_outreach'),
    path('health-services/', HealthServicesView.as_view(), name='health_services'),
    path('education-support/', EducationSupportView.as_view(), name='education_support'),
]