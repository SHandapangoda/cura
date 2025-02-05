from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CareSeekerSignupForm, CareProviderSignupForm, GuardianSignupForm
from .models import User

def care_seeker_signup(request):
    if request.method == 'POST':
        form = CareSeekerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(user.get_dashboard_url())  # Redirect based on role
    else:
        form = CareSeekerSignupForm()
    return render(request, 'users/signup_care_seeker.html', {'form': form})

def care_provider_signup(request):
    if request.method == 'POST':
        form = CareProviderSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(user.get_dashboard_url())
    else:
        form = CareProviderSignupForm()
    return render(request, 'users/signup_care_provider.html', {'form': form})

def guardian_signup(request):
    if request.method == 'POST':
        form = GuardianSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(user.get_dashboard_url())
    else:
        form = GuardianSignupForm()
    return render(request, 'users/signup_guardian.html', {'form': form})
def home(request):
    return render(request, 'users/home.html')