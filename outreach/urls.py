from django.urls import path
from . import views

app_name = 'outreach'

urlpatterns = [
    path('food-bank/', views.FoodBankView.as_view(), name='food_bank'),
]