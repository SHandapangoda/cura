from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CareSeekerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2']

class CareProviderSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    experience = forms.CharField(widget=forms.Textarea, required=True)  # Additional field for care providers
    education = forms.CharField(widget=forms.Textarea, required=True)  # Additional field for care providers

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'experience', 'education', 'password1', 'password2']


class GuardianSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=10, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    relationship_to_care_seeker = forms.CharField(max_length=100, required=True)  # Additional field for guardians

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'address', 'relationship_to_care_seeker', 'password1', 'password2']
