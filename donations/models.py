from django.db import models


class Donation(models.Model):
    DONATION_TYPES = [
        ('general', 'General Donation'),
        ('faith', 'Faith & Outreach'),
        ('health', 'Health Services'),
        ('water', 'Water & Sanitation'),
        ('education', 'Education Support'),
        ('food_bank', 'Food Bank'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES, default='general')
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"Donation of ${self.amount} by {self.donor_name}"
