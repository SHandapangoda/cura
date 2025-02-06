from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    relationship_to_care_seeker = models.CharField(max_length=100, blank=True, null=True)  # Additional field for guardians
    experience = forms.CharField(widget=forms.Textarea, required=True)  # Additional field for care providers
    education = forms.CharField(widget=forms.Textarea, required=True)  # Additional field for care providers

    def __str__(self):
        return self.email
