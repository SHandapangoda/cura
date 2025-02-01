from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CareSeekerSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'address']
        widgets = {
            'role': forms.HiddenInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'CARE_SEEKER'
        if commit:
            user.save()
        return user