from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    amount = forms.DecimalField(
        min_value=1.00,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter amount',
            'step': '0.01'
        })
    )

    class Meta:
        model = Donation
        fields = ['amount', 'donation_type', 'donor_name', 'donor_email', 'message', 'is_anonymous']
        widgets = {
            'donation_type': forms.Select(attrs={'class': 'form-control'}),
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'donor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional message'}),
            'is_anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }