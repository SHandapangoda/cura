from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None  # Remove default username
    email = models.EmailField(unique=True)  # Email is unique identifier
    email_verified = models.BooleanField(default=False)

    ROLE_CHOICES = [
        ('CARE_SEEKER', 'Care Seeker'),
        ('CARE_PROVIDER', 'Care Provider'),
        ('GUARDIAN', 'Care Seeker Guardian'),
        ('ADMIN', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = []  # Remove username requirement

    def get_dashboard_url(self):
        """Returns the landing page URL based on role"""
        if self.role == 'CARE_SEEKER':
            return 'care_seeker_dashboard'
        elif self.role == 'CARE_PROVIDER':
            return 'care_provider_dashboard'
        elif self.role == 'GUARDIAN':
            return 'guardian_dashboard'
        elif self.role == 'ADMIN':
            return 'admin_dashboard'
        return 'home'

    def __str__(self):
        return self.email
